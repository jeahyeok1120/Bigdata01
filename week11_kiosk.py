import kiosk as kk
#from kiosk import drinks, display_menu, order_process, print_receipt

if __name__ == "__main__":
    kk.run()
    kk.print_receipt()
    print(f"번호표 : {kk.get_ticket_number()}")