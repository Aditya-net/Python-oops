import streamlit as st

from main import Bank


def ensure_data_loaded():
    """Load data from disk once per run."""
    if not Bank.data:
        Bank.load()


def page_create_account():
    st.header("Create Account")
    with st.form("create_account"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, step=1)
        email = st.text_input("Email")
        pin = st.text_input("4-digit PIN", type="password", max_chars=4)
        submitted = st.form_submit_button("Create")

    if submitted:
        if not name or not email or not pin:
            st.error("All fields are required.")
            return

        if len(pin) != 4 or not pin.isdigit() or age < 18:
            st.error("Account cannot be created (invalid age or PIN). Age must be 18+ and PIN must be 4 digits.")
            return

        pin_int = int(pin)
        info = {
            "name": name,
            "age": int(age),
            "email": email,
            "pin": pin_int,
            "accountNo": Bank._accountgenerate(),
            "balance": 0,
        }

        Bank.data.append(info)
        Bank.update()

        st.success("Account created successfully! Please note down your account number.")
        st.json(info)


def _get_user(accnumber: str, pin: str):
    if not accnumber or not pin:
        return None, "Account number and PIN are required."
    if not pin.isdigit():
        return None, "Invalid PIN."
    pin_int = int(pin)
    userdata = [i for i in Bank.data if i["accountNo"] == accnumber and i["pin"] == pin_int]
    if not userdata:
        return None, "No account found with provided details."
    return userdata[0], None


def page_deposit():
    st.header("Deposit Money")
    with st.form("deposit_money"):
        accnumber = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password", max_chars=4)
        amount = st.number_input("Amount to deposit", min_value=0, step=1)
        submitted = st.form_submit_button("Deposit")

    if submitted:
        user, err = _get_user(accnumber, pin)
        if err:
            st.error(err)
            return

        if amount <= 0 or amount > 100000:
            st.error("Invalid deposit amount. Must be between 1 and 100000.")
            return

        user["balance"] += int(amount)
        Bank.update()
        st.success(f"Amount deposited successfully. New balance: {user['balance']}")


def page_withdraw():
    st.header("Withdraw Money")
    with st.form("withdraw_money"):
        accnumber = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password", max_chars=4)
        amount = st.number_input("Withdrawal amount", min_value=0, step=1)
        submitted = st.form_submit_button("Withdraw")

    if submitted:
        user, err = _get_user(accnumber, pin)
        if err:
            st.error(err)
            return

        if amount <= 0:
            st.error("Invalid amount.")
            return

        if user["balance"] < int(amount):
            st.error("Insufficient balance.")
            return

        user["balance"] -= int(amount)
        Bank.update()
        st.success(f"Amount withdrawn successfully. New balance: {user['balance']}")


def page_show_details():
    st.header("Show Account Details")
    with st.form("show_details"):
        accnumber = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password", max_chars=4)
        submitted = st.form_submit_button("Show Details")

    if submitted:
        user, err = _get_user(accnumber, pin)
        if err:
            st.error(err)
            return

        st.subheader("Account Details")
        st.json(user)


def page_update_details():
    st.header("Update Account Details")
    with st.form("update_details"):
        accnumber = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password", max_chars=4)
        new_name = st.text_input("New Name (leave blank to keep current)")
        new_email = st.text_input("New Email (leave blank to keep current)")
        new_pin = st.text_input("New 4-digit PIN (leave blank to keep current)", type="password", max_chars=4)
        submitted = st.form_submit_button("Update")

    if submitted:
        user, err = _get_user(accnumber, pin)
        if err:
            st.error(err)
            return

        if new_pin and (not new_pin.isdigit() or len(new_pin) != 4):
            st.error("Invalid PIN format. It must be 4 digits.")
            return

        if new_name:
            user["name"] = new_name
        if new_email:
            user["email"] = new_email
        if new_pin:
            user["pin"] = int(new_pin)

        Bank.update()
        st.success("Details updated successfully.")
        st.json(user)


def page_delete_account():
    st.header("Delete Account")
    with st.form("delete_account"):
        accnumber = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password", max_chars=4)
        confirm = st.checkbox("I confirm that I want to delete this account")
        submitted = st.form_submit_button("Delete")

    if submitted:
        if not confirm:
            st.warning("Please confirm deletion before proceeding.")
            return
        user, err = _get_user(accnumber, pin)
        if err:
            st.error(err)
            return

        Bank.data.remove(user)
        Bank.update()
        st.success("Account deleted successfully.")


def main():
    st.set_page_config(page_title="Bank Management System", layout="centered")
    st.title("Bank Management System (Web)")
    st.write("Use the sidebar to choose an action.")

    ensure_data_loaded()

    page = st.sidebar.radio(
        "Select Action",
        [
            "Create Account",
            "Deposit Money",
            "Withdraw Money",
            "Show Account Details",
            "Update Account Details",
            "Delete Account",
        ],
    )

    if page == "Create Account":
        page_create_account()
    elif page == "Deposit Money":
        page_deposit()
    elif page == "Withdraw Money":
        page_withdraw()
    elif page == "Show Account Details":
        page_show_details()
    elif page == "Update Account Details":
        page_update_details()
    elif page == "Delete Account":
        page_delete_account()


if __name__ == "__main__":
    main()

