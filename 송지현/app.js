window.onload = () => {
  let modalOpenBtn = document.querySelectorAll(".modal-open");
  let modalClosenBtn = document.querySelectorAll(".modal-close");

  modalOpenBtn.forEach((i) => {
    i.addEventListener("click", (event) => {
      let findName =
        event.target.parentElement.querySelector(".member-name").innerText;
      openMemberModal(findName);
    });
  });

  function openMemberModal(userName) {
    console.log(userName);
  }
};
