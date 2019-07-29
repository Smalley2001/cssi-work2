#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Replace "pass" with your code

class BankAccount(object):
    def __init__(self, label, balance):
        self.label = label
        self.balance = balance


    def __str__(self):
        return " Your account balance is: " + str(self.label) +str(self.balance)



    def Withdraw(self):
        withdrawAmount= raw_input(" How much would you like to withdraw: ")
        self.balance = self.balance - int(withdrawAmount)
        if self.balance<0:
            sel.balance= self.balance + int(withdrawAmount)
            print("You have an insufficient balance")
        else:
            print("Withdraw completed, Your summary balance is: " +str(self.balance))

    def Deposit(self):
        depositAmount= raw_input(" How much would you like to deposit: ")
        if int(depositAmount)<0:
            print(" Sorry, you can not deposit a negative amount")
        else:
            self.balance = self.balance + int(depositAmount)
            print(" Deposit completed, Your summary balance is: " + str(self.balance))


    def Rename(self):
        renameAccount= raw_input(" What would you like to change your account name to?")
        if renameAccount== " ":
            print(" You can't have name your account nothing")
        else:
            self.label=renameAccount
            print(" Your new account name is: " + renameAccount)

dorian_account= BankAccount("Dorian", 5000)
dorian_account.__str__()
dorian_account.Withdraw()
dorian_account.Deposit()
dorian_account.Rename()
