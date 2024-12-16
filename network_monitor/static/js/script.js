document.addEventListener("DOMContentLoaded", function () {
    function updateStatuses() {
        fetch("/check_status", { method: "POST" })
            .then((response) => response.json())
            .then((data) => {
                Object.keys(data).forEach((id) => {
                    const status = data[id];
                    const iconContainer = document.getElementById(`icon-container-${id}`);
                    const iconOnline = document.getElementById(`icon-online-${id}`);
                    const iconOffline = document.getElementById(`icon-offline-${id}`);
                    const iconUnstable = document.getElementById(`icon-unstable-${id}`);
                    const details = document.getElementById(`details-${id}`);

                    // Reset all icons
                    iconOnline.style.display = "none";
                    iconOffline.style.display = "none";
                    iconUnstable.style.display = "none";

                    // Show correct icon
                    if (status === "Online") {
                        iconOnline.style.display = "block";
                    } else if (status === "Offline") {
                        iconOffline.style.display = "block";
                    } else {
                        iconUnstable.style.display = "block";
                    }

                    // Apply animation classes
                    iconContainer.classList.add("show-icon");
                    details.classList.add("move-right");
                });
            })
            .catch((error) => console.error("Erro ao atualizar status:", error));
    }

    // Atualiza os status a cada 30 segundos
    setInterval(updateStatuses, 30000);

    // Chama uma vez no carregamento inicial
    updateStatuses();
});
