import numpy as np
import matplotlib.pyplot as plt

def objective_function(phase_control_vector, x_pos, y_pos, z_pos, original_amplitudes, original_phases, freq, c, target_theta, target_phi):
    phase_states = np.array([0, 90, 180, 270])    									# 定義可能的相位狀態
    phases = phase_states[phase_control_vector.astype(int)] 						# 根據相位控制向量選擇相位
    total_phases = original_phases + phases    										# 計算總相位
    element_weights = original_amplitudes * np.exp(1j * np.deg2rad(total_phases)) 	# 計算每個天線單元的權重
    af = array_factor(x_pos, y_pos, z_pos, element_weights, freq, c, [target_theta], [target_phi]) 	# 計算陣列因子
    af_db = 20 * np.log10(np.abs(af)) 					# 計算陣列因子的分貝值

    # 取得目標方向的增益
    boresight_gain = af_db[0,0]  						# 單一方向對應唯一值

    # 計算成本函數
    cost = -boresight_gain  							# 極大化增益
    return cost

def array_factor(x_pos, y_pos, z_pos, element_weights, freq, c, theta_scanning_angles, phi_scanning_angles):
    wavelength = c / freq    		# 計算波長
    k = 2 * np.pi / wavelength 		# 計算波數
    af = np.zeros((len(theta_scanning_angles), len(phi_scanning_angles)), dtype=complex) # 初始化陣列因子

    # 對每個 theta 和 phi 進行迭代計算
    for i, theta in enumerate(theta_scanning_angles):
        for j, phi in enumerate(phi_scanning_angles):
            # 計算相位因子
            psi = k * (x_pos * np.sin(np.deg2rad(theta)) * np.cos(np.deg2rad(phi)) +
                       y_pos * np.sin(np.deg2rad(theta)) * np.sin(np.deg2rad(phi)) +
                       z_pos * np.cos(np.deg2rad(theta)))

            af[i] += np.sum(element_weights * np.exp(1j * psi)) # 計算陣列因子
    return af


# Lu-250411 =================
print('GO ...')

from common import f_speed_up
speedup = f_speed_up()

from common import f_remove_report
f_remove_report()

from common import f_getIni_targetTheta
target_list = f_getIni_targetTheta()
# ===========================

for target_theta in target_list:
	# 陣列參數設定
	n_rows = 6
	n_columns = 6
	spacing = 0.0029

	# 創建 X 和 Y 的網格
	x_grid, y_grid = np.meshgrid(np.linspace(-spacing * (n_columns - 1) / 2, spacing * (n_columns - 1) / 2, n_columns),
	                             np.linspace(-spacing * (n_rows - 1) / 2, spacing * (n_rows - 1) / 2, n_rows))

	# 展平 X 和 Y 的網格坐標
	x_pos = x_grid.flatten()
	y_pos = y_grid.flatten()

	# 去除角落天線的位置
	corner_indices = [0, n_columns - 1, n_columns * (n_rows - 1), n_rows * n_columns - 1]
	x_pos = np.delete(x_pos, corner_indices)
	y_pos = np.delete(y_pos, corner_indices)

	# 只取前 32 個天線的位置
	x_pos = x_pos[:32]
	y_pos = y_pos[:32]
	z_pos = np.zeros_like(x_pos)

	# 原始的相位差和振幅
	original_phase_diff = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 180, 180, 0, 0, 0, 0, 180, 180, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
	amplitudes = np.array([0.895887318,0.92747035,0.899422296,0.908414847,0.891153975,0.927491552,0.890426524,0.925703657,0.820356812,0.917636505,0.727549986,0.73594118,0.806213214,0.847746554,0.633279655,0.925568592,0.924952507,0.939511881,0.752375156,0.86627518,0.898488077,0.881966737,0.801423801,0.890106663,0.905084251,0.859444004,0.809984704,0.883822395,0.870388752,0.884209172,0.801017539,0.92850962])
	phases = np.array([-110.0935841,-101.7858023,-110.212586,-109.433828,-105.8546589,-84.92967478,-98.35051209,-98.28538314,-100.4399018,-99.85577584,-81.99083436,-86.26897833,-82.39213682,-97.91620951,-113.9510586,-104.7759327,-85.4659197,-86.89973188,-66.44013557,-66.70638559,-84.91703197,-91.05910013,-84.96693211,-101.6550381,-94.84410979,-79.76158906,-82.18508913,-83.10339576,-99.91862615,-103.4772529,-100.6912992,-101.2901963])
	phases = original_phase_diff + phases
	amplitudes = amplitudes / np.sqrt(32)

	# 頻率和光速
	freq = 58.32e9
	c = 3e8
	theta_scanning_angles = np.arange(-90, 91, 1) 	# 掃描角度範圍
	phi_scanning_angles = np.array([0])  			# phi 角度設置

	# 設定目標方向
	# target_theta = 20 	# 目標 theta 角度
	target_phi = 0 		# 目標 phi 角度

	# 粒子群優化的主要參數
	n_vars = 32
	n_particles = 1000

	n_iterations = 50

	lb = np.zeros(n_vars)
	ub = 3 * np.ones(n_vars)

	# PSO 主循環
	best_global_cost = np.inf
	best_global_position = None

	particles = np.random.randint(0, 4, (n_particles, n_vars))
	velocities = np.zeros((n_particles, n_vars))
	p_best = particles.copy()
	p_best_cost = np.full(n_particles, np.inf)
	g_best, g_best_cost = p_best[0, :].copy(), np.inf

	for iter in range(n_iterations):
		for i in range(n_particles):
			cost = objective_function(particles[i, :], x_pos, y_pos, z_pos, amplitudes, phases, freq, c, target_theta, target_phi)
			if cost < p_best_cost[i]:
				p_best[i, :] = particles[i, :].copy()
				p_best_cost[i] = cost
			if cost < g_best_cost:
				g_best = particles[i, :].copy()
				g_best_cost = cost

		for i in range(n_particles):
			r1 = np.random.rand(n_vars)
			r2 = np.random.rand(n_vars)
			velocities[i, :] = 0.5 * velocities[i, :] + 2 * r1 * (p_best[i, :] - particles[i, :]) + 2 * r2 * (g_best - particles[i, :])
			particles[i, :] = particles[i, :] + velocities[i, :]
			particles[i, :] = np.clip(np.round(particles[i, :]), lb, ub)

			if speedup != 1:
				print(f'Theta {target_theta}, Iteration {iter + 1}: Best Cost = {g_best_cost}')

	if g_best_cost < best_global_cost:
		best_global_cost = g_best_cost
		best_global_position = g_best.copy()

	# 顯示所有試驗的結果
	print('Best Costs for all trials:')
	print(best_global_cost)

	# 計算最佳的相位控制向量
	phase_states = np.array([0, 90, 180, 270])
	best_phases = phase_states[best_global_position.astype(int)]

	print('\n==== 相位控制資訊 ===')
	print('Best phase control vector(0,1,2,3):')
	print(best_global_position.astype(int))
	print(best_phases)

	print('\n=== 波束掃描角度資訊 ===')
	print(f'目標方向: θ = {target_theta}°, φ = {target_phi}°')

	# 計算最終的天線權重
	final_element_weights = amplitudes * np.exp(1j * np.deg2rad(phases + best_phases))
	af = array_factor(x_pos, y_pos, z_pos, final_element_weights, freq, c, theta_scanning_angles, phi_scanning_angles)
	af_db = 20 * np.log10(np.abs(af))

	# 確定 boresight_gain 的索引
	theta_index = np.where(theta_scanning_angles == target_theta)[0][0]
	phi_index = np.where(phi_scanning_angles == target_phi)[0][0]
	boresight_gain = af_db[theta_index, phi_index]
	print(f'Boresight Gain (dB): {boresight_gain:.2f}')

	# 畫圖顯示陣列幾何和陣列因子
	fig, (ax_geometry, ax_response) = plt.subplots(1, 2, figsize=(12, 6))

	# 陣列幾何
	ax_geometry.scatter(x_pos, y_pos, c='b', edgecolor='k', label='Elements')
	ax_geometry.set_title('Array Geometry')
	ax_geometry.set_xlabel('X Position (m)')
	ax_geometry.set_ylabel('Y Position (m)')
	ax_geometry.axis('equal')
	ax_geometry.grid(True, which='both')
	ax_geometry.legend()

	# 陣列因子
	ax_response.plot(theta_scanning_angles, af_db, linewidth=2, color='b', label='Array Factor')
	ax_response.set_xlabel(r'$\theta$ (degrees)')
	ax_response.set_ylabel('Array Pattern (dB)')
	ax_response.set_title('Array Factor Response')
	ax_response.grid(True)
	ax_response.set_ylim([-30, 30])
	ax_response.axvline(x=target_theta, color='r', linestyle='--', label=f'Target θ={target_theta}°')
	ax_response.legend()

	plt.tight_layout()

	# Lu-250408 =================
	from common import f_establish_directory
	from common import f_get_clock
	from pathlib import Path
	p = f_establish_directory()
	t = f_get_clock()
	f = 'report_' + str(target_theta) + '_' + t + '.png'
	pf = Path(str(p) + '\\' + f)

	plt.savefig(pf, dpi=300, bbox_inches='tight')
	# ===========================

	# plt.show()

print('DONE ...')
