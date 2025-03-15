```javascript
document.addEventListener("contextmenu", (event) => event.preventDefault());

function checkPin() {
  const pin = document.getElementById("pin").value;
  if (pin === "1999") {
    const encryptedFlag = [
      67, 83, 67, 50, 53, 123, 72, 52, 114, 100, 67, 48, 100, 51, 100, 95, 74,
      52, 118, 52, 115, 99, 114, 49, 112, 116, 95, 83, 51, 99, 114, 51, 116, 125,
    ];
    const flag = encryptedFlag.map((c) => String.fromCharCode(c)).join("");
    document.getElementById("flag").innerText = flag;
    document.getElementById("flag").style.display = "block";
  } else {
    alert("PIN është gabim! Provoni përsëri.");
  }
}
```
