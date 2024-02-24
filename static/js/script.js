function addInputFields() {
    var newDiv = document.createElement("div");
    newDiv.classList.add("row", "mb-3");

    newDiv.innerHTML = `
    <div class="col">
      <input type="text" class="form-control" name="medicine[]" placeholder="Medicine Name">
    </div>
    <div class="col">
      <input type="text" class="form-control" name="time[]" placeholder="Time">
    </div>
    <div class="col">
      <button type="button" class="btn btn-danger" onclick="deleteInputField(this)">Delete</button>
    </div>
  `;

    document.getElementById("inputsContainer").appendChild(newDiv);
}

function deleteInputField(button) {
    var row = button.closest(".row");
    row.remove();
}