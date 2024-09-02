const button = document.getElementById("open-modal")
button.addEventListener("click", openModal)

function openModal() {
    const modalWrapper = document.getElementById("modal-wrapper")
    modalWrapper.classList.add("modal-is-open")
}
