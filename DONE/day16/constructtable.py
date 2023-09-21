from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name",("pikachu","squirtle","charmander"))
table.add_column("Type",("electric","water","fire"))
table.align="c"




print(table)