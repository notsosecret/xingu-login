const button = document.getElementById("openModal")
button.addEventListener("click", openModal)

function openModal() {
    const modalWrapper = document.getElementById("modalWrapper")
    modalWrapper.classList.add("modal-open")
}
