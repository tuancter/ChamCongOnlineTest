function searchEmployee() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("searchInput");
    filter = input.value.toUpperCase();
    table = document.querySelector(".employee-table");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows and hide those that don't match the search query
    for (i = 1; i < tr.length; i++) { // start from 1 to skip header row
        td = tr[i].getElementsByTagName("td")[0]; // the first column is Name
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
}
