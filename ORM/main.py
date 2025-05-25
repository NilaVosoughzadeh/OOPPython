from models.user import User

User.create_table()

print(" ایجاد کاربر جدید ")
name = input("نام: ").strip()
email = input("ایمیل: ").strip()

if not email :
    print("ایمیل نمی تواند خالی باشد")
    exit(1)

user = User(name=name, email=email)
try:
    user.save()
    print(user.id, "کاربر ذخیره شد با شناسه:")
except ValueError as ve:
    print(ve, "خطا در ذخیره سازی کاربر")
    exit(1)

print("\n دریافت کاربر ")
search_email = input("ایمیل کاربر برای جستجو: ")

user = User.get(email=search_email)
if user:
    print("کاربر یافت شد:")
    print(f"نام: {user.name} | ایمیل: {user.email}")

    update = input(" می‌خواهید نام کاربر را ویرایش کنید؟ (بله / خیر):")
    if update.lower() == 'بله':
        new_name = input("نام جدید: ").strip()
        user.name = new_name
        try:
            user.save()
            print("نام جدید ذخیره شد.")
        except ValueError as ve:
            print(ve, "خطا در به روزرسانی کاربر")

    delete = input(" می‌خواهید این کاربر را حذف کنید؟ (بله / خیر):")
    if delete.lower() == 'بله':
        user.delete()
        print("کاربر حذف شد.")
else:
    print("کاربری با این ایمیل پیدا نشد.")