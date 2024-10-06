document.getElementById("now").addEventListener("change", setCurrentDate);
document.getElementById("inThreeDays").addEventListener("change", function() { setFutureDate(3); });
document.getElementById("inAWeek").addEventListener("change", function() { setFutureDate(7); });
document.getElementById("inAMonth").addEventListener("change", setFutureMonth);

function setCurrentDate() {
    const today = new Date();
    const formattedDate = formatDate(today);
    document.getElementById("now").value = formattedDate;
    updateSelectedValue(formattedDate);
}

function setFutureDate(days) {
    const today = new Date();
    today.setDate(today.getDate() + days); 
    const formattedDate = formatDate(today);
    if (days === 3) {
        document.getElementById("inThreeDays").value = formattedDate; 
        updateSelectedValue(formattedDate); 
    } else if (days === 7) {
        document.getElementById("inAWeek").value = formattedDate;
        updateSelectedValue(formattedDate);
    }
}

function setFutureMonth() {
    const today = new Date();
    today.setMonth(today.getMonth() + 1);
    const formattedDate = formatDate(today);
    document.getElementById("inAMonth").value = formattedDate; 
    updateSelectedValue(formattedDate);
}

function formatDate(date) {
    const day = String(date.getDate()).padStart(2, '0');
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const year = date.getFullYear();
    return `${year}-${month}-${day}`;
}

function updateSelectedValue(value) {
    document.getElementById("selectedValue").innerText = value;
}