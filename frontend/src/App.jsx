import { useState } from 'react';
import './App.css';
import api from './services/api';
function App() {
  
  const [jobDescription,setJobDescription]=useState("");
  const [resumeFile,setResumeFile]=useState(null);
  const [analysisResult,setAnalysisResult]=useState(null);
  const [loading,setLoading]=useState(false);
  const handleAnalyze=async () => {
    setLoading(true)
    console.log("Analyze button clicked!")
    const formdata=new FormData()
    formdata.append("file",resumeFile)
    formdata.append("job_description",jobDescription)
    try{
        const response=await api.post("/ats/analyze",formdata)
        setAnalysisResult(response.data)
    } catch(error){ 
        console.error(error)
    }
    finally{
      setLoading(false)
    }
    
  }
  
  return (
    <div className='app'>
      <div className='container'>
        <h1>🤖 AI Resume Intelligence Platform</h1>
        <p className='subtitle'>Smart ATS Analysis & Resume Optimization</p>
        <div className='upload-section'>
          <p>
            Upload your resume and analyze it against any job description.
          </p>
          <h3>Resume</h3>
          <label className='file-upload'>
            <input type="file" onChange={(e)=>setResumeFile(e.target.files[0])}/>
            <span>📤 Upload Resume</span>
          </label>
          {
            resumeFile && (
              <p className='file-name'>
                📁{resumeFile.name}
              </p>
            )
          }
          
          <h3>Paste Job Description</h3>
          <textarea rows="10" cols="60" placeholder="Paste the complete job description here..." value={jobDescription} onChange={(e)=>setJobDescription(e.target.value)}></textarea>
          
          <button onClick={handleAnalyze} disabled={loading}>{loading?"Analyzing...":"Analyze Resume"}</button>
        </div>
        <div className='results-section'>
        {
          analysisResult && (
            <div className='results-grid'>
              <div className='score-card'>
                <h2>ATS Score </h2>
                
                <p>{analysisResult.ats_score}%</p>
              </div>
              <div className='matched-card'>
                <h2>Matched Skills</h2>
                <ul>
                  {
                    analysisResult.matched_skills.map((skill)=>(
                        <li key={skill.name}>
                          ✔ {skill.name}
                        </li>
                    ))
                  }
                </ul>
              </div>
              <div className='missing-card'>
                <h2>Missing Skills</h2>
                <ul>
                  {
                    analysisResult.missing_skills.map((skill)=>(
                        <li key={skill.name}>
                          ❌ {skill.name}
                        </li>
                    ))
                  }
                </ul>
              </div>
              <div className='extra-card'>
                <h2>Extra Skills</h2>
                <ul>
                  {
                    analysisResult.extra_skills.map((skill)=>(
                        <li key={skill.name}>
                          ⭐ {skill.name}
                        </li>
                    ))
                  }
                </ul>
              </div>
              <div className='feedback-card'>
                <h2>AI Feedback</h2>
              
                <h3>Strengths</h3>
                <ul>
                  {
                    analysisResult.ai_feedback.strengths.map((strength)=>(
                        <li key={strength}>
                          💪 {strength}
                        </li>
                    ))
                  }
                </ul>
                <h3>Weaknesses</h3>
                <ul>
                  {
                    analysisResult.ai_feedback.weaknesses.map((weak)=>(
                        <li key={weak}>
                          ⚠️ {weak}
                        </li>
                    ))
                  }
                </ul>
                <h3>Resume Improvements</h3>
                <ul>
                  {
                    analysisResult.ai_feedback.resume_improvements.map((imp)=>(
                        <li key={imp}>
                          📝 {imp}
                        </li>
                    ))
                  }
                </ul>
                <h3>Keyword Suggestions</h3>
                <ul>
                  {
                    analysisResult.ai_feedback.keyword_suggestions.map((sug)=>(
                        <li key={sug}>
                          🔑 {sug}
                        </li>
                    ))
                  }
                </ul>
                <h3>Missing Skill Suggestions</h3>
                <ul>
                  {
                    analysisResult.ai_feedback.missing_skill_suggestions.map((missing)=>(
                        <li key={missing}>
                          🎯 {missing}
                        </li>
                    ))
                  }
                </ul>
                <h3>Interview Questions</h3>
                <ul>
                {
                  analysisResult.ai_feedback.interview_questions.map((iq)=>(
                      <li key={iq}>
                        ❓ {iq}
                      </li>
                  ))
                }
                </ul>
              </div>

            </div>
          )
        }
        </div>
      </div>
      
    </div>
  )
}

export default App
