document.addEventListener("DOMContentLoaded", () => {
            const calendar = document.getElementById("calendar");
            const today = new Date();

            const year = today.getFullYear();
            const month = today.getMonth(); // 0–11

            // Số ngày trong tháng
            const daysInMonth = new Date(year, month + 1, 0).getDate();

            // Thứ của ngày 1 trong tháng (0=CN, 1=Thứ 2...)
            let firstDay = new Date(year, month, 1).getDay();

            // Đổi về hệ bắt đầu từ Thứ 2
            firstDay = firstDay === 0 ? 6 : firstDay - 1;

            // Tạo ô trống trước ngày 1
            for (let i = 0; i < firstDay; i++) {
                const empty = document.createElement("span");
                empty.classList.add("empty");
                calendar.appendChild(empty);
            }

            // In ngày
            for (let day = 1; day <= daysInMonth; day++) {
                const span = document.createElement("span");
                span.textContent = day;

                // Highlight hôm nay
                if (
                    day === today.getDate() &&
                    month === today.getMonth() &&
                    year === today.getFullYear()
                ) {
                    span.classList.add("today");
                }

                calendar.appendChild(span);
            }
        });