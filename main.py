import os
from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse
from app.rag import get_context
from app.llm_router import generate_math_problem

app = FastAPI(title="MathGen-RAG Dashboard")

@app.post("/generate")
def trigger_generation(topic: str = Form(...), model: str = Form(...)):
    try:
        # Retrieve context from your committed local database
        context_docs = get_context(topic, k=2)
        generated_output = generate_math_problem(model, topic, context_docs)
        return {"output": generated_output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/", response_class=HTMLResponse)
def serve_ui():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>MathGen-RAG Workspace</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <script>
            window.MathJax = {
                tex : {
                    inlineMath: [['$', '$'], ['\\(', '\\)']],
                    displayMath: [['$$', '$$'], ['\\[', '\\]']]
                }
            };
        </script>
        <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
        <script>
            tailwind.config = {
                theme: { extend: { colors: { jeeDark: '#0f172a', jeeBlue: '#2563eb' } } }
            }
        </script>
    </head>
    <body class="bg-slate-50 min-h-screen text-slate-800">

        <header class="bg-jeeDark text-white shadow-md py-4 px-6 mb-8 border-b border-slate-800">
            <div class="max-w-6xl mx-auto flex justify-between items-center">
                <div class="flex items-center gap-3">
                    <div class="bg-jeeBlue p-2 rounded-lg text-white">
                        <i class="fa-solid fa-square-root-variable text-xl"></i>
                    </div>
                    <div>
                        <h1 class="text-lg font-bold tracking-tight">MathGen-RAG</h1>
                        <p class="text-xs text-slate-400">JEE Advanced Conceptual Problem Factory</p>
                    </div>
                </div>
                <div class="text-xs bg-slate-800 text-slate-300 px-3 py-1.5 rounded-full border border-slate-700">
                    <span class="inline-block w-2 h-2 bg-emerald-500 rounded-full mr-2 animate-pulse"></span>Vercel Production Active
                </div>
            </div>
        </header>

        <main class="max-w-6xl mx-auto px-4 grid grid-cols-1 lg:grid-cols-3 gap-8 pb-12">
            
            <section class="lg:col-span-1 bg-white p-6 rounded-xl shadow-sm border border-slate-200 h-fit">
                <h2 class="text-base font-bold text-slate-900 mb-4 flex items-center gap-2">
                    <i class="fa-solid fa-sliders text-jeeBlue"></i> Workspace Parameters
                </h2>
                
                <form id="genForm" class="space-y-4">
                    <div>
                        <label class="block text-xs font-semibold text-slate-500 uppercase tracking-wider mb-1.5">Model Blueprint</label>
                        <div class="relative">
                            <select name="model" id="model" class="w-full bg-slate-50 border border-slate-300 rounded-lg p-3 pr-10 text-sm focus:outline-none focus:ring-2 focus:ring-jeeBlue appearance-none font-medium">
                                <option value="gemini-flash-lite">⚡ Gemini 2.5 Flash</option>
                            </select>
                            <i class="fa-solid fa-chevron-down absolute right-3 top-4 text-slate-400 pointer-events-none text-xs"></i>
                        </div>
                    </div>

                    <div>
                        <label class="block text-xs font-semibold text-slate-500 uppercase tracking-wider mb-1.5">Target Math Concept</label>
                        <input type="text" name="topic" id="topic" 
                               placeholder="e.g., Triangle inequalities or Complex rotation" 
                               class="w-full bg-slate-50 border border-slate-300 rounded-lg p-3 text-sm focus:outline-none focus:ring-2 focus:ring-jeeBlue font-medium" required>
                    </div>

                    <button type="button" onclick="generateQuestion()" class="w-full bg-jeeBlue hover:bg-blue-700 transition text-white font-bold py-3 px-4 rounded-lg shadow flex items-center justify-center gap-2">
                        <i class="fa-solid fa-wand-magic-sparkles"></i> Synthesize Problem
                    </button>
                </form>
            </section>

            <section class="lg:col-span-2 flex flex-col gap-6">
                
                <div id="placeholderState" class="bg-white rounded-xl border border-dashed border-slate-300 p-12 text-center text-slate-400 my-auto shadow-sm">
                    <i class="fa-solid fa-chart-pie text-4xl mb-3 text-slate-300"></i>
                    <p class="text-sm font-medium text-slate-600">No Active Pipeline Execution</p>
                    <p class="text-xs text-slate-400 max-w-xs mx-auto mt-1">Specify a target chapter sub-concept on the left sidebar controls and initiate synthesis.</p>
                </div>

                <div id="loadingState" class="hidden bg-white rounded-xl border border-slate-200 p-12 text-center shadow-sm">
                    <div class="animate-spin inline-block w-8 h-8 border-[3px] border-current border-t-transparent text-jeeBlue rounded-full mb-3"></div>
                    <p class="text-sm font-medium text-slate-700">Extracting context structures from Vector Ingestion Storage...</p>
                    <p class="text-xs text-slate-400 mt-1">Prompting cloud production endpoints.</p>
                </div>

                <div id="contentWorkspace" class="hidden space-y-6">
                    <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
                        <div class="flex items-center gap-2 border-b border-slate-100 pb-3 mb-4">
                            <span class="bg-amber-100 text-amber-800 text-xs px-2 py-0.5 rounded font-bold uppercase tracking-wide">Problem Statement</span>
                        </div>
                        <div id="problemText" class="text-slate-800 leading-relaxed font-sans whitespace-pre-wrap"></div>
                    </div>

                    <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
                        <div class="flex items-center gap-2 border-b border-slate-100 pb-3 mb-4">
                            <span class="bg-emerald-100 text-emerald-800 text-xs px-2 py-0.5 rounded font-bold uppercase tracking-wide">Verification Path</span>
                        </div>
                        <div id="solutionText" class="text-slate-800 leading-relaxed font-sans whitespace-pre-wrap"></div>
                    </div>
                </div>
            </section>
        </main>

        <script>
            // Helper function to convert markdown syntax to HTML formatting tags
            function formatMarkdown(text) {
                if (!text) return "";
                return text
                    .replace(/\\\*\\\*(.*?)\\\*\\\*/g, '<strong>$1</strong>') // Matches **bold**
                    .replace(/\\\*(.*?)\\\*/g, '<em>$1</em>');               // Matches *italics*
            }

            async function generateQuestion() {
                const placeholder = document.getElementById('placeholderState');
                const loading = document.getElementById('loadingState');
                const workspace = document.getElementById('contentWorkspace');
                
                placeholder.classList.add('hidden');
                loading.classList.remove('hidden');
                workspace.classList.add('hidden');

                const formData = new FormData();
                formData.append('topic', document.getElementById('topic').value);
                formData.append('model', document.getElementById('model').value);

                try {
                    const res = await fetch('/generate', { method: 'POST', body: formData });
                    const data = await res.json();
                    
                    const fullText = data.output;
                    let probPart = fullText;
                    let solPart = "No step-by-step solution breakdown separated by model constraints.";

                    if(fullText.includes('### STEP-BY-STEP SOLUTION')) {
                        const splitArr = fullText.split('### STEP-BY-STEP SOLUTION');
                        probPart = splitArr[0].replace('### PROBLEM', '').trim();
                        solPart = splitArr[1].trim();
                    } else if (fullText.includes('### SOLUTION')) {
                        const splitArr = fullText.split('### SOLUTION');
                        probPart = splitArr[0].replace('### PROBLEM', '').trim();
                        solPart = splitArr[1].trim();
                    }

                    // CHANGED: Run formatting wrappers and change innerText to innerHTML
                    document.getElementById('problemText').innerHTML = formatMarkdown(probPart);
                    document.getElementById('solutionText').innerHTML = formatMarkdown(solPart);

                    loading.classList.add('hidden');
                    workspace.classList.remove('hidden');

                    // Trigger MathJax re-render for incoming raw text strings
                    MathJax.typesetPromise();

                } catch (err) {
                    alert("Pipeline execution error. Verify network stability.");
                    loading.classList.add('hidden');
                    placeholder.classList.remove('hidden');
                }
            }
        </script>
    </body>
    </html>
    """