document.addEventListener("DOMContentLoaded", () => {
	const popupLinks = document.querySelectorAll(".popup-link");
	const body = document.body;
	const unlock = true;

	// Открытие попапа
	if (popupLinks.length > 0) {
		popupLinks.forEach((link) => {
			link.addEventListener("click", (e) => {
				e.preventDefault();
				const targetId = link.getAttribute("href").substring(1);
				const targetPopup = document.getElementById(targetId);
				if (targetPopup) popupOpen(targetPopup);
			});
		});
	}

	// Закрытие попапа
	document.addEventListener("click", (e) => {
		if (e.target.classList.contains("popup__close") || e.target.classList.contains("popup__area")) {
			const popup = e.target.closest(".popup");
			if (popup) popupClose(popup);
		}
	});

	// Закрытие по Esc
	document.addEventListener("keydown", (e) => {
		if (e.key === "Escape") {
			const openPopup = document.querySelector(".popup.open");
			if (openPopup) popupClose(openPopup);
		}
	});

	function popupOpen(popup) {
		if (popup && unlock) {
			const activePopup = document.querySelector(".popup.open");
			if (activePopup) popupClose(activePopup);

			body.classList.add("lock");
			popup.classList.add("open");
		}
	}

	function popupClose(popup) {
		popup.classList.remove("open");
		body.classList.remove("lock");
	}
});
