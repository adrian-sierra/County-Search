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
  CRIMINAL_OFFENSES,
  TRAFFIC_OFFENSES,
  CIVIL_OFFENSES,
} from "./random_record_variables.js";

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
  if (randomNum === 3) {
    return "Criminal";
  } else if (randomNum === 2) {
    return "Civil";
  }
  return "Traffic";
}

function randomOffense(case_type) {
  if (case_type == "Civil") {
    return randomElementSelector(CIVIL_OFFENSES);
  } else if (case_type == "Criminal") {
    return randomElementSelector(CRIMINAL_OFFENSES);
  } else if (case_type == "Traffic") {
    return randomElementSelector(TRAFFIC_OFFENSES);
  } else {
    return "Unknown case type.";
  }
}

function randomOffenseDate(date_of_birth) {
  let day_of_birth = parseInt(date_of_birth.split("/")[0]);
  let month_of_birth = parseInt(date_of_birth.split("/")[1]);
  let year_of_birth = parseInt(date_of_birth.split("/")[2]);
  let random_day = Math.floor(Math.random() * (31 - 1) + 1);
  let random_month = Math.floor(Math.random() * (12 - 1) + 1);
  let random_year = Math.floor(
    Math.random() * (2024 - (year_of_birth + 18)) + (year_of_birth + 18)
  );
  while (
    random_year === year_of_birth &&
    random_month <= month_of_birth &&
    random_day < day_of_birth
  ) {
    random_day = Math.floor(Math.random() * (31 - 1) + 1);
    random_month = Math.floor(Math.random() * (12 - 1) + 1);
    random_year = Math.floor(
      Math.random() * (2024 - (year_of_birth + 18)) + (year_of_birth + 18)
    );
  }

  return random_month + "/" + random_day + "/" + random_year;
}

export {
  randomPlaintiff,
  randomLastName,
  randomFirstName,
  randomMiddleName,
  randomAddress,
  randomDateOfBirth,
  randomCitationNumber,
  randomCaseStatus,
  randomCaseType,
  randomOffense,
  randomOffenseDate,
};
