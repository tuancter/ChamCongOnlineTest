// Open modal for editing state
function openModal() {
    document.getElementById('editStateModal').style.display = 'flex';
}

// Close modal
function closeModal() {
    document.getElementById('editStateModal').style.display = 'none';
}
// Mở modal khi nhấn Sửa
function openEditModal() {
    document.getElementById("editModal").style.display = "flex";
}

// Đóng modal khi nhấn Hủy
function closeModal() {
    document.getElementById("editModal").style.display = "none";
}

// Lưu thay đổi và cập nhật thông tin
function saveChanges() {
    // Lấy dữ liệu từ các ô input
    const empName = document.getElementById("emp-name-input").value;
    const empDob = document.getElementById("emp-dob-input").value;
    const empAddress = document.getElementById("emp-address-input").value;
    const empPhone = document.getElementById("emp-phone-input").value;
    const empPosition = document.getElementById("emp-position-input").value;
    const empSalary = document.getElementById("emp-salary-input").value;
    const empStatus = document.getElementById("emp-status-input").value;
    const empTimeIn = document.getElementById("emp-time-in-input").value;
    const empTimeOut = document.getElementById("emp-time-out-input").value;

    // Cập nhật thông tin vào bảng
    document.getElementById("emp-name").innerText = empName;
    document.getElementById("emp-dob").innerText = empDob;
    document.getElementById("emp-address").innerText = empAddress;
    document.getElementById("emp-phone").innerText = empPhone;
    document.getElementById("emp-position").innerText = empPosition;
    document.getElementById("emp-salary").innerText = empSalary;
    document.getElementById("emp-status").innerText = empStatus;
    document.getElementById("emp-time-in").innerText = empTimeIn;
    document.getElementById("emp-time-out").innerText = empTimeOut;

    // Đóng modal sau khi lưu
    closeModal();
}
