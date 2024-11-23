
def show_menu_principal():

    while True:
        print("\n")
        print("="*45)
        print("         Simulador de Gasto Diario")
        print("="*45)
        print("Seleccione una opción:")
        print("\n1. Registrar nuevo gasto")
        print("2. Listar gastos")
        print("3. Calcular total de gastos")
        print("4. Generar reporte de gastos")
        print("5. Salir")
        print("="*45)

        option = input("Enter a valid option:  ").strip()
        match option:
            case "1":
                register_new_bill()
            case "2":
                call_bills()
            case "3":
                calculate_total_bills()
            case "4":
                generate_report_bills()
            case "5":
                print("thanks for use the 'BILLS SIMULATOR' have a good one")
            case _:
                print("\nERROR, choose a valid option !!!")
                
show_menu_principal()