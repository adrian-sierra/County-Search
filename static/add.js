import {
  CIVIL_PLAINTIFF_FIRST,
  CIVIL_PLAINTIFF_SECOND,
  CIVIL_PLAINTIFF_THIRD,
  CRIMINAL_PLAINTIFF,
  FIRST_NAMES,
  LAST_NAMES,
  MIDDLE_NAMES,
  STREET_NAMES,
  STREET_DIRECTIONS,
  STREET_SUFFIX,
  CITY_NAMES,
  STATES,
} from "./randomRecordVars.js";

function randomElementSelector(list) {
  return list[Math.floor(Math.random() * list.length)];
}

function randomPlaintiff(case_type) {
  if (case_type == "Criminal" || case_type == "Traffic") {
    return CRIMINAL_PLAINTIFF;
  } else if (case_type == "Civil") {
    return (
      randomElementSelector(CIVIL_PLAINTIFF_FIRST) +
      " " +
      randomElementSelector(CIVIL_PLAINTIFF_SECOND) +
      " " +
      randomElementSelector(CIVIL_PLAINTIFF_THIRD)
    );
  } else {
    return "Unknown case type.";
  }
}

function randomLastName() {
  return randomElementSelector(LAST_NAMES);
}

function randomFirstName() {
  return randomElementSelector(FIRST_NAMES);
}

function randomMiddleName() {
  if (Math.floor(Math.random() * (10 + 1) - 1) != 1) {
    return randomElementSelector(MIDDLE_NAMES);
  }
  return "";
}

function randomAddress() {
  function randomPostalCode() {
    let postalCode = Math.floor(Math.random() * (9999 - 501) + 501);
    let stringPostalCode;
    if (postalCode < 1000) {
      stringPostalCode = "00";
    } else if (postalCode < 10000) {
      stringPostalCode = "0";
    }
    stringPostalCode = stringPostalCode + postalCode.toString();
    return stringPostalCode;
  }
  return (
    Math.floor(Math.random() * (9999 - 1) + 1) +
    " " +
    randomElementSelector(STREET_NAMES) +
    " " +
    randomElementSelector(STREET_SUFFIX) +
    " " +
    randomElementSelector(STREET_DIRECTIONS) +
    ", " +
    randomElementSelector(CITY_NAMES) +
    ", " +
    randomElementSelector(STATES) +
    " " +
    randomPostalCode()
  );
}

function randomDateOfBirth() {
  return (
    Math.floor(Math.random() * (12 - 1) + 1) +
    "/" +
    Math.floor(Math.random() * (31 - 1) + 1) +
    "/" +
    Math.floor(Math.random() * (2006 - 1924) + 1924)
  );
}

function randomCitationNumber() {
  return Math.floor(Math.random() * (9999999999 - 999999999) + 999999999);
}

function randomCaseStatus() {
  if (Math.floor(Math.random())) {
    return "Closed";
  }
  return "Open";
}

function randomCaseType() {
  let randomNum = Math.floor(Math.random() * (4 - 1) + 1);
  console.log("random num: " + randomNum);
  if (randomNum === 3) {
    return "Criminal";
  } else if (randomNum === 2) {
    return "Civil";
  }
  return "Traffic";
}

function randomOffense() {}

function randomOffenseDate() {}

function randomOffenseType() {}

const randomRecordButton = document.getElementById("random-record-button");

function onRandomRecordClick() {
  let caseType = randomCaseType();
  console.log("Random plaintiff: " + randomPlaintiff(caseType));
  console.log("Random last name: " + randomLastName());
  console.log("Random first name: " + randomFirstName());
  console.log("Random middle name: " + randomMiddleName());
  console.log("Random address: " + randomAddress());
  console.log("Random date of birth: " + randomDateOfBirth());
  console.log("Random citation number: " + randomCitationNumber());
  console.log("Random case status: " + randomCaseStatus());
  console.log("Random case type: " + caseType);
  console.log("Random offense: " + randomOffense());
  console.log("Random offense date: " + randomOffenseDate());
  console.log("Random offense type: " + randomOffenseType());
}

randomRecordButton.addEventListener("click", onRandomRecordClick);
