let income = 0;
let expense = 0;

function addTransaction() {
  const amountInput = document.getElementById("amount");
  const typeInput = document.getElementById("type");
  const transactionsList = document.getElementById("transactions");

  const amount = parseFloat(amountInput.value);
  const type = typeInput.value;

  if (isNaN(amount) || amount <= 0) {
    alert("Please enter a valid amount.");
    return;
  }

  const li = document.createElement("li");
  if (type === "income") {
    income += amount;
    li.textContent = `Income: ₹${amount}`;
    li.style.color = "green";
  } else {
    expense += amount;
    li.textContent = `Expense: ₹${amount}`;
    li.style.color = "red";
  }

  transactionsList.appendChild(li);
  amountInput.value = "";

  updateSummary();
}

function updateSummary() {
  document.getElementById("income").textContent = income;
  document.getElementById("expense").textContent = expense;
  document.getElementById("savings").textContent = income - expense;
}
