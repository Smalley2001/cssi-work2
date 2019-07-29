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

#Milestone 1: Continually asking user for actions until they type "exit"
#Milestone 2: Add support for adding items to your list
#Milestone 3: Add supporting for printing everything
#Milestone 4: Add support for check if item is in the shopping_list
#Milestone 5: Add support for removing items
#Bonus: You can't have duplicate items on your list

shopping_list= []

#Adding to list

while True:
        selection= raw_input(" Do you want to add, remove, check, list, or exit? ")
        if selection== "add":
            item= raw_input("What would you like to add? ")
            shopping_list.append(item)

        elif selection== "remove":
            item = raw_input("What would you like to remove? ")
            shopping_list.remove(item)
        elif selection== "check":
            item= raw_input( "What would you like to check? ")
            if item in shopping_list:
                print("The item is in your shopping cart!")
            else:
                print(" The item is not in your shopping cart ")
        elif selection== "list":
            print(shopping_list)
        elif selection== "exit":
            break









#
#
# if selection== "yes" or "y":
#         print(" What would you like to add? ")
# if selection== "no" or "n":
#         print("Exit" + str(selection))
# else:
#         print(" Please make a choice? ")
#
# break
# print(selection)

# choice = ""
#
# print("Welcome to the shopping list app!")
#
# shopping_list = []
#
# while choice.lower() != "e":
#     print("Please choose your action from the following list:")
#     print("a. Add an item to the list")
#     print("b. Remove an item from the list")
#     print("c. Check to see if an item is on the list")
#     print("d. Show all items on the list")
#     print("e. exit")
#
#     choice = raw_input("Enter your choice [a|b|c|d|e]:")

    # Your code below! Handle the cases when the user chooses a, b, c, d, or e
