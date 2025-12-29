const password = document.getElementById("password");
const confirmPassword = document.getElementById("confirmPassword");
const errorText = document.getElementById("passwordError");

password.addEventListener("input", () => {
    if (confirmPassword.value !== "" && password.value !== confirmPassword.value) {
        errorText.style.display = "block";
        confirmPassword.setCustomValidity("Mật khẩu không khớp");
    } else {
        errorText.style.display = "none";
        confirmPassword.setCustomValidity("");
    }
});

confirmPassword.addEventListener("input", () => {
    if (password.value !== confirmPassword.value) {
        errorText.style.display = "block";
        confirmPassword.setCustomValidity("Mật khẩu không khớp");
    } else {
        errorText.style.display = "none";
        confirmPassword.setCustomValidity("");
    }
});

document.querySelector("form").addEventListener("submit", (e) => {
    if (password.value !== confirmPassword.value) {
        e.preventDefault();
        errorText.style.display = "block";
        confirmPassword.focus();
    }
});
