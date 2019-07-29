// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Task 1

const printAppointment = (dogName, time) => {
  return "I will walk " + dogName + " today at " + time;

}
const dogName1 = "Steve";
const dogType1 = "beagle";

if (dogName1=== "Steve"){
  console.log (printAppointment(dogName1,"12:00PM"))
}
// Complete Task 1 Below

const dogName2 = "Joe";
const dogType2 = "bulldog";

// Complete Task 2 Below
if (dogName2=== "corgi"){
  printAppointment (dogName2, "12")
}
if (dogName2==="bulldog") {
  printAppointment(dogName2,"1")
}
else {
  printAppointment(dogName2, "2")
}
const dogName3 = "Lola";
const dogType3 = "poodle";

// Complete Task 3 Below
if (dogName3=== "Spike"|| "Lola"|| "Jeremy"|| "Peaches"|| "Steve") {
  console.log ("I will walk " + dogName3 + " ,one of my favorite dogs, today at 1:00pm")
}
