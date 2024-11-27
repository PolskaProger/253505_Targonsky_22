let sortDirection = 1;
let currentPage = 1;
const rowsPerPage = 3;

document.addEventListener('DOMContentLoaded', function() {
    // Fetch categories if needed
    // fetchCategories();
});

document.getElementById('addButton').addEventListener('click', function(event) {
    event.preventDefault();
    const form = document.getElementById('addForm');
    const urlInput = document.getElementById('image');
    const phoneInput = document.getElementById('phone');
    if (validateURL(urlInput.value) && validatePhone(phoneInput.value)) {
        addDoctorToTable();
    } else {
        if (!validateURL(urlInput.value)) {
            urlInput.classList.add('invalid');
        }
        if (!validatePhone(phoneInput.value)) {
            phoneInput.classList.add('invalid');
        }
        showValidationMessage('Please fix the errors in the form.');
    }
});

function addDoctorToTable() {
    const form = document.getElementById('addForm');
    const last_name = form.last_name.value;
    const first_name = form.first_name.value;
    const image = form.image.value;
    const category = form.category.value;
    const phone = form.phone.value;
    const email = form.email.value;

    // AJAX POST request to add doctor to database
    fetch('/add-doctor/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({
            last_name: last_name,
            first_name: first_name,
            image: image,
            category: category,
            phone: phone,
            email: email,
        }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        if (data.success) {
            // Add new row to the table
            const tbody = document.getElementById("contactsTable").tBodies[0];
            const newRow = tbody.insertRow();

            // Create checkbox cell
            const checkboxCell = newRow.insertCell(0);
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.name = 'select';
            checkboxCell.appendChild(checkbox);

            // Create cells for each field
            const nameCell = newRow.insertCell(1);
            nameCell.textContent = last_name + ' ' + first_name;

            const imageCell = newRow.insertCell(2);
            const img = document.createElement('img');
            img.src = image;
            img.alt = last_name;
            img.width = '200';
            img.height = '200';
            imageCell.appendChild(img);

            const categoryCell = newRow.insertCell(3);
            categoryCell.textContent = category;

            const phoneCell = newRow.insertCell(4);
            phoneCell.textContent = phone;

            const emailCell = newRow.insertCell(5);
            emailCell.textContent = email;

            // Reset form and hide validation message
            form.reset();
            hideValidationMessage();
            document.getElementById('addButton').disabled = true;
        } else {
            showValidationMessage(data.error);
        }
    })
    .catch(error => {
        console.error('Error adding doctor:', error);
        showValidationMessage('An error occurred. Please try again later.');
    });
}

document.getElementById('addForm').addEventListener('input', function() {
    const form = this;
    const addButton = document.getElementById('addButton');
    if (addButton) {
        const inputs = form.querySelectorAll('input[required], select[required]');
        const allFilled = Array.from(inputs).every(input => input.value.trim() !== '');
        const urlInput = document.getElementById('image');
        const phoneInput = document.getElementById('phone');
        const isURLValid = validateURL(urlInput.value);
        const isPhoneValid = validatePhone(phoneInput.value);
        addButton.disabled = !(allFilled && isURLValid && isPhoneValid);
    }
});

document.getElementById('image').addEventListener('input', function() {
    const urlInput = this;
    const url = urlInput.value;
    if (!validateURL(url)) {
        urlInput.classList.add('invalid');
        showValidationMessage('Invalid URL.');
    } else {
        urlInput.classList.remove('invalid');
        hideValidationMessage();
    }
});

function validateURL(url) {
    const urlPattern = /^(https?:\/\/)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$/;
    return urlPattern.test(url);
}

function validatePhone(phone) {
    const phonePattern = /^(\+375|8)(12|25|29|33|44)[0-9]{7}$/;
    return phonePattern.test(phone);
}

document.getElementById('phone').addEventListener('input', function() {
    const phoneInput = this;
    const phone = phoneInput.value;
    if (!validatePhone(phone)) {
        phoneInput.classList.add('invalid');
        showValidationMessage('Invalid phone number.');
    } else {
        phoneInput.classList.remove('invalid');
        hideValidationMessage();
    }
});

function showValidationMessage(message) {
    const messageDiv = document.getElementById('validationMessage');
    if (!messageDiv) return;
    messageDiv.innerText = message;
    messageDiv.style.display = 'block';
}

function hideValidationMessage() {
    const messageDiv = document.getElementById('validationMessage');
    if (!messageDiv) return;
    messageDiv.innerText = '';
    messageDiv.style.display = 'none';
}

function sortTable(col) {
    const table = document.getElementById("contactsTable");
    if (!table) return;
    const rows = Array.from(table.tBodies[0].children);
    rows.sort((a, b) => {
        let valA = a.cells[col].innerText.toLowerCase();
        let valB = b.cells[col].innerText.toLowerCase();
        return sortDirection * (valA.localeCompare(valB));
    });
    table.tBodies[0].append(...rows);
    sortDirection *= -1;
}

function prevPage() {
    if (currentPage > 1) {
        currentPage--;
        displayRows();
    }
}

function nextPage() {
    const tbody = document.getElementById("contactsTable").tBodies[0];
    if (!tbody) return;
    const totalRows = tbody.children.length;
    const totalPages = Math.ceil(totalRows / rowsPerPage);
    if (currentPage < totalPages) {
        currentPage++;
        displayRows();
    }
}

function displayRows() {
    const tbody = document.getElementById("contactsTable").tBodies[0];
    if (!tbody) return;
    const rows = Array.from(tbody.children);
    rows.forEach((row, index) => {
        if (index >= (currentPage - 1) * rowsPerPage && index < currentPage * rowsPerPage) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}

function filterTable() {
    const input = document.getElementById("filterInput");
    if (!input) return;
    const filterValue = input.value.toLowerCase();
    const tbody = document.getElementById("contactsTable").tBodies[0];
    if (!tbody) return;
    const rows = tbody.children;
    for (let row of rows) {
        let match = false;
        for (let cell of row.cells) {
            if (cell.innerText.toLowerCase().includes(filterValue)) {
                match = true;
                break;
            }
        }
        row.style.display = match ? '' : 'none';
    }
    // Reset page to 1 when filtering
    currentPage = 1;
    displayRows();
}

function showDetails(pk) {
    console.log(`Showing details for doctor with ID: ${pk}`);
}

function redirectToDetail(pk) {
    window.location.href = `/doctor/${pk}/`;
}

function generateReward() {
    const selectedRows = document.querySelectorAll("#contactsTable tbody tr input:checked");
    const names = Array.from(selectedRows).map(row => row.nextElementSibling.innerText);
    document.getElementById("rewardMessage").innerText = `Rewarding: ${names.join(", ")}`;
}

// Function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}