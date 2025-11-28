async function analyzeTasks() {
    try {
        const tasks = JSON.parse(document.getElementById("taskInput").value);
        const strategy = document.getElementById("strategy").value;

        const response = await fetch("/api/analyze/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ tasks, strategy })
        });

        const result = await response.json();

        let html = "";
        result.forEach(t => {
            html += `
                <div class="task-card">
                    <h3>${t.title}</h3>
                    <p><b>Due:</b> ${t.due_date}</p>
                    <p><b>Effort:</b> ${t.estimated_hours} hrs</p>
                    <p><b>Importance:</b> ${t.importance}/10</p>
                    <p><b>Dependencies:</b> ${t.dependencies.length}</p>
                    <p><b>Priority Score:</b> <span class="${getPriorityColor(t.priority_score)}">${t.priority_score.toFixed(2)}</span></p>
                    <hr />
                </div>
            `;
        });

        document.getElementById("output").innerHTML = html;

    } catch (err) {
        alert("Invalid JSON format!");
    }
}

function getPriorityColor(score) {
    if (score >= 50) return "high";
    if (score >= 25) return "medium";
    return "low";
}
