document.addEventListener("DOMContentLoaded", () => {
  const dropArea = document.getElementById("dropArea");
  const fileInput = document.getElementById("resumeFiles");
  const fileList = document.getElementById("fileList");

  // Handle Drag & Drop Events
  dropArea.addEventListener("dragover", (event) => {
    event.preventDefault();
    dropArea.classList.add("dragover");
  });

  dropArea.addEventListener("dragleave", () => {
    dropArea.classList.remove("dragover");
  });

  dropArea.addEventListener("drop", (event) => {
    event.preventDefault();
    dropArea.classList.remove("dragover");

    const files = event.dataTransfer.files;
    handleFiles(files);
  });

  fileInput.addEventListener("change", () => {
    handleFiles(fileInput.files);
  });

  function handleFiles(files) {
    fileList.innerHTML = "";
    for (let file of files) {
      const fileItem = document.createElement("p");
      fileItem.textContent = file.name;
      fileList.appendChild(fileItem);
    }
  }
});

// Upload Resumes Function
function uploadResumes() {
  const files = document.getElementById("resumeFiles").files;
  const loadingDiv = document.getElementById("loading");
  const resultsDiv = document.getElementById("results");

  if (files.length === 0) {
    alert("Please upload at least one resume.");
    return;
  }

  loadingDiv.classList.remove("hidden");
  resultsDiv.innerHTML = ""; // Clear previous results

  setTimeout(() => {
    loadingDiv.classList.add("hidden");

    let resultsHTML = `<h3 class="text-xl font-bold text-green-400">Ranked Candidates:</h3>`;
    let fakeData = ["John Doe", "Jane Smith", "Alex Johnson"];
    fakeData.forEach((name, index) => {
      resultsHTML += `
        <div class="mt-3 p-4 bg-gray-700 rounded-lg">
          <p class="text-lg font-semibold">${index + 1}. ${name}</p>
          <p class="text-sm text-gray-300">Score: ${Math.floor(
            Math.random() * 100
          )}</p>
        </div>
      `;
    });

    resultsDiv.innerHTML = resultsHTML;
  }, 2000);
}
