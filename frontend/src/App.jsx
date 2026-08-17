import { useEffect, useState } from "react";
import "./App.css";

const API_URL = "https://bounty-finder-96hk.onrender.com/api/opportunities/";

function App() {
  const [opportunities, setOpportunities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchOpportunities = async () => {
    try {
      setLoading(true);
      setError(null);

      const response = await fetch(API_URL);

      if (!response.ok) {
        throw new Error("Failed to fetch opportunities");
      }

      const data = await response.json();
      setOpportunities(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchOpportunities();
  }, []);

  return (
    <div className="app">
      <header className="header">
        <div>
          <h1>Bounty Finder</h1>
          <p>Personal developer opportunity radar</p>
        </div>

        <button onClick={fetchOpportunities}>
          ↻ Refresh
        </button>
      </header>

      <main>
        <section className="stats">
          <div className="stat-card">
            <span>Opportunities</span>
            <strong>{opportunities.length}</strong>
          </div>

          <div className="stat-card">
            <span>High Match</span>
            <strong>
              {
                opportunities.filter(
                  (opportunity) => opportunity.skill_match >= 70
                ).length
              }
            </strong>
          </div>
        </section>

        {loading && (
          <div className="message">
            Finding bounties...
          </div>
        )}

        {error && (
          <div className="message error">
            {error}
          </div>
        )}

        {!loading && !error && (
          <section className="opportunities">
            {opportunities.map((opportunity, index) => (
              <article
                className="opportunity-card"
                key={`${opportunity.url}-${index}`}
              >
                <div className="card-top">
                  <span className="source">
                    {opportunity.source}
                  </span>

                  <span className="match">
                    {opportunity.skill_match > 0
                      ? `${opportunity.skill_match}% match`
                      : "No match"}
                  </span>
                </div>

                <h2>{opportunity.title}</h2>

                <div className="reward">
                  {opportunity.reward !== null
                    ? `${opportunity.reward} ${
                        opportunity.currency || ""
                      }`
                    : "Reward unknown"}
                </div>

                {opportunity.skills.length > 0 && (
                  <div className="skills">
                    {opportunity.skills.map((skill) => (
                      <span key={skill}>{skill}</span>
                    ))}
                  </div>
                )}

                <a
                  href={opportunity.url}
                  target="_blank"
                  rel="noreferrer"
                >
                  View Bounty →
                </a>
              </article>
            ))}
          </section>
        )}
      </main>
    </div>
  );
}

export default App;