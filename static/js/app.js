// Handle recruiter form submission
document.getElementById("recruiterForm")?.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = {
        name: document.getElementById("name").value,
        experience: parseInt(document.getElementById("experience").value, 10),
        skills: document.getElementById("skills").value,
        job_description: document.getElementById("job_description").value,
    };

    try {
        const response = await fetch("/generate/recruiter", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formData),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const result = await response.json();
        document.getElementById("result").innerHTML = `<pre>${result.email}</pre>`;
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("result").innerText = "Failed to generate email. Please check the console for details.";
    }
});

// Handle candidate form submission
document.getElementById("candidateForm")?.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = {
        name: document.getElementById("name").value,
        experience: parseInt(document.getElementById("experience").value, 10),
        skills: document.getElementById("skills").value,
        job_description: document.getElementById("job_description").value,
    };

    try {
        const response = await fetch("/generate/candidate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(formData),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const result = await response.json();
        document.getElementById("result").innerHTML = `<pre>${result.email}</pre>`;
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("result").innerText = "Failed to generate email. Please check the console for details.";
    }
});