"""
Contact Book

Tavsif:
    Bu dastur kontaktlar bilan ishlaydi — qo‘shish, ko‘rish, qidirish va
    email bo‘yicha filtrlash. Har bir kontakt "Ism|Telefon|Email" formatida
    list ichida string sifatida saqlanadi.
"""

from typing import List


def show_menu() -> None:
    """Konsolda foydalanuvchi uchun menyuni chiqaradi."""
    print("\n====== 📱 Contact Book v2.2 ======")
    print("1. ➕ Yangi kontakt qo‘shish")
    print("2. 📄 Barcha kontaktlarni ko‘rish")
    print("3. 🔍 Kontaktni ism bo‘yicha qidirish")
    print("4. 📧 Faqat @gmail.com kontaktlarni ko‘rish")
    print("5. 🚪 Dasturni yakunlash")


def is_valid_contact(contact: list) -> bool:
    """
    Kontakt formati to‘g‘ri yoki noto‘g‘ri ekanligini aniqlaydi.

    Args:
        contact (str): Kontakt string (masalan, "Ali|99890...|ali@gmail.com").

    Returns:
        bool: To‘g‘ri format bo‘lsa True, aks holda False.
    """
    pass


def add_contact(contact_list: List[list]) -> None:
    """
    Yangi kontakt qo‘shadi.

    Args:
        contact_list (List[str]): Kontaktlar ro‘yxati.
    """
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    new_contact = [name, phone, email]
    contact_list.append(new_contact)
    print("Kontakt qoshildi !")

def list_contacts(contact_list: List[list]) -> None:
    """
    Kontaktlar ro‘yxatini konsolga chiqaradi.

    Args:
        contact_list (List[str]): Kontaktlar ro‘yxati.
    """
    if contact_list != []:
        print("Barcha kontaktlar:")
        for contact in contact_list:
            print(f"{contact[0]} - {contact[1]} - {contact[2]}")
        else:
            print("Kontaklar mavjud emas")


def search_contact(contact_list: List[list]) -> None:
    """
    Foydalanuvchi kiritgan ism bo‘yicha kontaktlarni qidiradi.

    Args:
        contact_list (List[str]): Kontaktlar ro‘yxati.
    """
    search = input("Search: ")
    for contact in contact_list:
        if search.lower() in contact[0].lower():
            print(f"{contact[0]} - {contact[1]} - {contact[2]}")


def filter_gmail_contacts(contact_list: List[list]) -> None:
    """
    Faqat @gmail.com domeniga ega kontaktlarni ko‘rsatadi.

    Args:
        contact_list (List[str]): Kontaktlar ro‘yxati.
    """
    for contact in contact_list:
        if contact[2].endswith("@gmail.com"):
            print(f"{contact[0]} - {contact[1]} - {contact[2]}")
    


def main() -> None:
    """
    Dasturning asosiy ishga tushirish funksiyasi.
    Menyu orqali foydalanuvchi tanlovini boshqaradi.
    """
    contacts: List[list] = []

    while True:
        show_menu()
        choice = input("Tanlov (1–5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            list_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            filter_gmail_contacts(contacts)
        elif choice == "5":
            print("👋 Dasturni yakunlayapmiz. Xayr!")
            break
        else:
            print("❗️Noto‘g‘ri tanlov. Iltimos, 1 dan 5 gacha son kiriting.")


main()
