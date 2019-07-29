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

const AlarmClock=() => {
  return (alarmMessage)
}
console.log ("My alarm!");

const My_Alarm= (time) => {
  console.log (" Hey, Dorian, wake up! It's " +time)
}
console.log (My_Alarm(" 12:00pm "));

const Mom_Alarm= (time) => {
  console.log (" Hey, Mom, wake up! It's " +time)
}
console.log (Mom_Alarm( " 8:00am "));

const Family_Alarm= (name, time) => {
  console.log (" Hey " +name+ " wake up! It's " +time)
}
console.log (Family_Alarm("Dorian", " 6:00am "));

const Important_Alarm= (message) => {
  return (message.toUpperCase());
}
console.log (Important_Alarm(" wake up! wake up! wake Up!! "));

const Snooze_Alarm= (time) => {
  let newTime= time +1;
  return " The alarm for " + time + " has been changed to " + newTime;
}
