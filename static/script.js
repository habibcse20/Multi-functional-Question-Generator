function switchTab(tabName) {
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.content').forEach(c => c.classList.remove('active'));

    document.getElementById(tabName + '-tab').classList.add('active');
    document.getElementById(tabName).classList.add('active');
}

function toggleAnswer(btn) {
    const ans = btn.nextElementSibling;
    if (ans.style.display === "none") {
        ans.style.display = "block";
        btn.innerText = "Hide Answer";
    } else {
        ans.style.display = "none";
        btn.innerText = "Show Answer";
    }
}

