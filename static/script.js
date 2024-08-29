const button = document.getElementById("openModal")
button.addEventListener("click", openModal)

function openModal() {
    const overlay = document.getElementById("overlay")
    overlay.style.display = "block"
    const modal = document.getElementById("modal")
    modal.style.display = "block"
}
