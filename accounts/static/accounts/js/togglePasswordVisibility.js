/*
    Hàm hiện thị đóng mở mật khẩu khi user nhất kiểm tra
*/
function togglePasswordVisibility(icon) {
    const inputId = icon.dataset.target;
    const input = document.getElementById(inputId);

    if (input.type === "password") {
        input.type = "text";
        icon.innerText = "visibility";
    } else {
        input.type = "password";
        icon.innerText = "visibility_off";
    }
}

