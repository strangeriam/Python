Create a text widget with tk.Text.
The "height" property is the number of rows.

The starting position is "1.0" and the ending position is "end".

Insert with ".insert("1.0", "Text...")" and retrieve with ".get("1.0", "end")".

test["state"] = "disabled" will prevent typing. Otherwise use "normal".
