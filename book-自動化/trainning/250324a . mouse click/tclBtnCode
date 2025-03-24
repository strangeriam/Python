
;# TCL/TK code
;# ===========
console show

proc _f_time_get {} {
	clock format [clock seconds] -format "%y%m%d %H:%M:%S"
}

frame .f1 -background gray -relief ridge -borderwidth 100 -height 200 -width 600
::ttk::button .f1.btn1 -text "normal" -command { puts "normal .. [_f_time_get]" }
::ttk::button .f1.btn2 -text "active" -default "active" -command { puts "active .. [_f_time_get]" }
::ttk::button .f1.btn3 -text "exit" -command { puts "exit" ; exit}
pack .f1.btn1 .f1.btn2 .f1.btn3 -fill both
pack .f1
