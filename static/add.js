import {
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
} from "./random_data_functions.js";

const randomRecordButton = document.getElementById("random-record-button");

function onRandomRecordClick() {
  const case_type = randomCaseType();
  let date_of_birth = randomDateOfBirth();

  document.getElementById("plaintiff").value = randomPlaintiff(case_type);
  document.getElementById("last-name").value = randomLastName();
  document.getElementById("first-name").value = randomFirstName();
  document.getElementById("middle-name").value = randomMiddleName();
  document.getElementById("address").value = randomAddress();
  document.getElementById("dob").valueAsDate = date_of_birth;
  document.getElementById("citation-number").value = randomCitationNumber();
  document.getElementById("case-status").value = randomCaseStatus();
  document.getElementById("case-type").value = case_type;

  const offenses_group = document.querySelectorAll(".offense-group");
  // let number_of_offenses;
  // if (case_type == "Civil") {
  //   number_of_offenses = 1;

  // } else {
  //   number_of_offenses = offenses_group.length;
  // }
  // console.log(number_of_offenses);

  // for (let i = 0; i < number_of_offenses; i++) {
  //   const random_offense = randomOffense(case_type);
  //   offenses_group[i].querySelector('[name="offense"]').value =
  //     random_offense[0];
  //   offenses_group[i].querySelector('[name="offense-date"]').valueAsDate =
  //     randomOffenseDate(date_of_birth);
  //   offenses_group[i].querySelector('[name="offense-type"]').value =
  //     random_offense[1];
  // }
  offenses_group.forEach((offense_group) => {
    const random_offense = randomOffense(case_type);
    offense_group.querySelector('[name="offense"]').value = random_offense[0];
    offense_group.querySelector('[name="offense-date"]').valueAsDate =
      randomOffenseDate(date_of_birth);
    offense_group.querySelector('[name="offense-type"]').value =
      random_offense[1];
  });
}

randomRecordButton.addEventListener("click", onRandomRecordClick);

const addOffenseButton = document.getElementById("add-offense-button");
const removeOffenseButton = document.getElementById("remove-offense-button");

function onAddOffenseButtonClick() {
  document
    .getElementById("add-form-div")
    .appendChild(document.querySelector(".offense-group").cloneNode(true));

  removeOffenseButton.style.display = "inline-block";
}

function onRemoveOffenseButtonClick() {
  if (document.querySelectorAll(".offense-group").length == 2) {
    removeOffenseButton.style.display = "none";
  }
  const offenses_group = document.querySelectorAll(".offense-group");
  document
    .getElementById("add-form-div")
    .removeChild(offenses_group[offenses_group.length - 1]);
}

addOffenseButton.addEventListener("click", onAddOffenseButtonClick);
removeOffenseButton.addEventListener("click", onRemoveOffenseButtonClick);

// const addFormButton = document.getElementById("add-form-button");

// function onAddFormButtonClick(e) {
//   e.preventDefault();
//   console.log(document.getElementById("case-type").value);
// }

// addFormButton.addEventListener("click", onAddFormButtonClick);
