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

    bank_name: str = Field(description="The name of the bank. e.g. 'Bank of America'")
    bank_address: str = Field(
        description="The address of the bank. e.g. '123 Main St, Anytown, USA'"
    )

    account_holder_name: str = Field(
        description="The name of the account holder. e.g. 'John Doe'"
    )
    account_holder_address: str = Field(
        description="The address of the account holder. e.g. '123 Main St, Anytown, USA'"
    )
    account_number: str = Field(description="The account number. e.g. '1234567890'")

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

    transactions: List[Transaction] = Field(
        description="The transactions in the statement"
    )
