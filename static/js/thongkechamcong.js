let currentRowId = null;

// Chức năng tìm kiếm theo ngày
function searchAttendance() {
    var inputDate = document.getElementById('searchDate').value;
    var table = document.getElementById('attendanceData');
    var rows = table.getElementsByTagName('tr');
    
    // Lọc các dòng trong bảng theo ngày
    for (var i = 0; i < rows.length; i++) {
        var cells = rows[i].getElementsByTagName('td');
        if (cells.length > 0) {
            var dateCell = cells[0].textContent || cells[0].innerText;
            if (dateCell.includes(inputDate)) {
                rows[i].style.display = '';
            } else {
                rows[i].style.display = 'none';
            }
        }
    }
}

// Chức năng chỉnh sửa chấm công
function editAttendance(rowId) {
    currentRowId = rowId;
    
    // Lấy dữ liệu từ các ô trong dòng hiện tại
    var row = document.getElementById("row-" + rowId);
    var status = row.querySelector(".status").innerText;
    var startTime = row.querySelector(".start-time").innerText;
    var endTime = row.querySelector(".end-time").innerText;

    // Điền dữ liệu vào modal
    document.getElementById("status").value = status;
    document.getElementById("start-time").value = startTime;
    document.getElementById("end-time").value = endTime;

    // Hiển thị modal
    document.getElementById("editModal").style.display = "flex";
}

// Chức năng lưu thay đổi
function saveChanges() {
    var status = document.getElementById("status").value;
    var startTime = document.getElementById("start-time").value;
    var endTime = document.getElementById("end-time").value;

    // Cập nhật lại các ô trong bảng với dữ liệu mới
    var row = document.getElementById("row-" + currentRowId);
    row.querySelector(".status").innerText = status;
    row.querySelector(".start-time").innerText = startTime;
    row.querySelector(".end-time").innerText = endTime;

    // Đóng modal sau khi lưu
    closeModal();
}

// Đóng modal
function closeModal() {
    document.getElementById("editModal").style.display = "none";
}
