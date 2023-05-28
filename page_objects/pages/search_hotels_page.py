from test_utility.utility_methods import UtilMethods
from page_objects.locators.search_hotel_page_locator import SearchHotelPageLocator


class SearchHotelPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.util_obj = UtilMethods(self.driver)
        self.location_dropdown_xpath = SearchHotelPageLocator.location_dropdown_xpath
        self.hotels_dropdown_xpath = SearchHotelPageLocator.hotels_dropdown_xpath
        self.room_type_dropdown_xpath = SearchHotelPageLocator.room_type_dropdown_xpath
        self.number_of_rooms_dropdown_xpath = SearchHotelPageLocator.number_of_rooms_dropdown_xpath
        self.check_in_date_input_text_box_xpath = SearchHotelPageLocator.check_in_date_input_text_box_xpath
        self.check_out_date_input_text_box_xpath = SearchHotelPageLocator.check_out_date_input_text_box_xpath
        self.adult_rooms_dropdown_xpath = SearchHotelPageLocator.adult_rooms_dropdown_xpath
        self.child_rooms_dropdown_xpath = SearchHotelPageLocator.child_rooms_dropdown_xpath
        self.search_button_xpath = SearchHotelPageLocator.search_button_xpath
        self.reset_button_xpath = SearchHotelPageLocator.reset_button_xpath

        self.search_radio_button_xpath = SearchHotelPageLocator.search_radio_button_xpath
        self.continue_button_xpath = SearchHotelPageLocator.continue_button_xpath
        self.cancel_button_xpath = SearchHotelPageLocator.cancel_button_xpath
        # Booking locator
        self.first_name_text_box_xpath = SearchHotelPageLocator.first_name_text_box_xpath
        self.last_name_text_box_xpath = SearchHotelPageLocator.last_name_text_box_xpath
        self.billing_address_text_box_xpath = SearchHotelPageLocator.billing_address_text_box_xpath
        self.credit_card_text_box_xpath = SearchHotelPageLocator.credit_card_text_box_xpath
        self.credit_card_type_dropdown_xpath = SearchHotelPageLocator.credit_card_type_dropdown_xpath
        self.expiry_date_moth_dropdown_xpath = SearchHotelPageLocator.expiry_date_moth_dropdown_xpath
        self.expiry_date_year_dropdown_xpath = SearchHotelPageLocator.expiry_date_year_dropdown_xpath
        self.cvv_number_text_box_xpath = SearchHotelPageLocator.cvv_number_text_box_xpath
        self.book_now_button_xpath = SearchHotelPageLocator.book_now_button_xpath
        self.book_cancel_button_xpath = SearchHotelPageLocator.book_cancel_button_xpath

        self.log_out_xpath = SearchHotelPageLocator.log_out_xpath

    def search_for_hotels_and_book_in_sydney(self):
        # This TC for Booking the Hotels
        self.util_obj.dropdown_visible_text(self.location_dropdown_xpath, "Sydney")
        self.util_obj.dropdown_visible_text(self.hotels_dropdown_xpath, "Hotel Sunshine")
        self.util_obj.dropdown_visible_text(self.room_type_dropdown_xpath, "Double")
        self.util_obj.dropdown_visible_text(self.number_of_rooms_dropdown_xpath, "4 - Four")
        self.util_obj.send_keys(self.check_in_date_input_text_box_xpath, "28/05/2023")
        self.util_obj.send_keys(self.check_out_date_input_text_box_xpath, "31/05/2023")
        self.util_obj.dropdown_visible_text(self.adult_rooms_dropdown_xpath, "3 - Three")
        self.util_obj.dropdown_visible_text(self.child_rooms_dropdown_xpath, "2 - Two")
        self.util_obj.click_on_element(self.search_button_xpath)
        self.util_obj.click_on_element(self.search_radio_button_xpath)
        self.util_obj.click_on_element(self.continue_button_xpath)
        booking_page_url = "https://adactinhotelapp.com/BookHotel.php"
        if self.driver.current_url == booking_page_url:
            result1 = True
            print("</br>", "Booking Page Loading Successfully....", "</br>")
        else:
            result1 = False
            print("</br>", "Booking Page Loading Failed....", "</br>")
        self.util_obj.send_keys(self.first_name_text_box_xpath,"Chris")
        self.util_obj.send_keys(self.last_name_text_box_xpath,"Max")
        self.util_obj.send_keys(self.billing_address_text_box_xpath,"South Africa")
        self.util_obj.send_keys(self.credit_card_text_box_xpath,"8523697894561236")
        self.util_obj.dropdown_visible_text(self.credit_card_type_dropdown_xpath,"VISA")
        self.util_obj.dropdown_visible_text(self.expiry_date_moth_dropdown_xpath,"May")
        self.util_obj.dropdown_visible_text(self.expiry_date_year_dropdown_xpath,"2025")
        self.util_obj.send_keys(self.cvv_number_text_box_xpath,"123")
        self.util_obj.click_on_element(self.book_now_button_xpath)
        booking_confirm = "https://adactinhotelapp.com/BookingConfirm.php"
        if self.driver.current_url == booking_confirm:
            result2 = True
            print("</br>","Booking Confirmed...",self.driver.current_url,"</br>")
        else:
            result2 = False
            print("</br>", "Booking Failed....",self.driver.current_url, "</br>")

        self.util_obj.click_on_element(self.log_out_xpath)

        if result1 and result2:
            result = True
        else:
            result = False

        return result