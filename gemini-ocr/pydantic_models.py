from pydantic import BaseModel, Field
from typing import List


class Transaction(BaseModel):
    transaction_date: str = Field(
        description="The date of the transaction in 'YYYY-MM-DD' format. e.g. '01/01/2021'"
    )
    transaction_amount: float = Field(
        description="The amount of the transaction. e.g. '1000.00'"
    )
    transaction_type: str = Field(
        description="The type of the transaction. e.g. 'Deposit' or 'Withdrawal'"
    )
    transaction_description: str = Field(
        description="The description of the transaction"
    )


class BankStatement(BaseModel):
    # bank info
    bank_name: str = Field(description="The name of the bank. e.g. 'Bank of America'")
    bank_address: str = Field(
        description="The address of the bank. e.g. '123 Main St, Anytown, USA'"
    )
    # account info
    account_holder_name: str = Field(
        description="The name of the account holder. e.g. 'John Doe'"
    )
    account_holder_address: str = Field(
        description="The address of the account holder. e.g. '123 Main St, Anytown, USA'"
    )
    account_number: str = Field(description="The account number. e.g. '1234567890'")
    # statement info
    statement_start_date: str = Field(
        description="The start date of the statement in 'YYYY-MM-DD' format. e.g. '2021-01-01'"
    )
    statement_end_date: str = Field(
        description="The end date of the statement in 'YYYY-MM-DD' format. e.g. '2021-01-01'"
    )
    statement_beginning_balance: float = Field(
        description="The beginning balance of the statement. e.g. '1000.00'"
    )
    statement_ending_balance: float = Field(
        description="The ending balance of the statement. e.g. '1000.00'"
    )
    # transactions
    transactions: List[Transaction] = Field(
        description="The transactions in the statement"
    )


class DriverLicense(BaseModel):
    license_number: str = Field(
        description="The driver license number. e.g. 'D12345678'"
    )
    expiration_date: str = Field(
        description="The expiration date of the license in 'YYYY-MM-DD' format. e.g. '2025-01-01'"
    )
    first_name: str = Field(
        description="The first name of the license holder (sometimes shown as 'FN' on the license). e.g. 'John'"
    )
    last_name: str = Field(
        description="The last name of the license holder (sometimes shown as 'LN' on the license). e.g. 'Doe'"
    )
    date_of_birth: str = Field(
        description="The date of birth of the license holder in 'YYYY-MM-DD' format. e.g. '1990-01-01'"
    )
