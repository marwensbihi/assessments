import React, { useEffect, useState } from 'react';
import axios from 'axios';

const NearbyAirports = () => {
  const [airports, setAirports] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchNearbyAirports = async () => {
      setLoading(true);
      setError(null);

      try {
        const response = await axios.get('https://sky-scrapper.p.rapidapi.com/api/v1/flights/getNearByAirports', {
          params: {
            lat: 36.507226,
            lng: 	8.775656,
            locale: 'en-US',
          },
          headers: {
            'x-rapidapi-host': 'sky-scrapper.p.rapidapi.com',
            'x-rapidapi-key': 'a2b248e679mshf3d81a9f8bc1905p1aef76jsnc9d679aa735c',
          },
        });

        console.log('API Response:', response.data); // For debugging

        if (response.data?.status) {
          // Accessing nearby airports properly based on the API response
          const nearbyAirports = response.data.data.nearby;
          setAirports(nearbyAirports || []);
        } else {
          setError('No nearby airports found.');
        }
      } catch (err) {
        setError('An error occurred while fetching nearby airports. Please try again.');
        console.error('API Error:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchNearbyAirports();
  }, []); // Remove lat and lng if they're hardcoded

  return (
    <div className="nearby-airports-container">
      {loading && <p className="loading-message">Loading nearby airports...</p>}
      {error && <p className="error-message">{error}</p>}
      {!loading && !error && airports.length > 0 && (
        <div>
          <h2>Nearby Airports</h2>
          <div className="airport-card-container">
            {airports.map((airport, index) => (
              <div key={index} className="airport-card">
                <h3>{airport.presentation.title}</h3>
                <p>{airport.skyId}</p>
                <p>{airport.presentation.subtitle}</p>
              </div>
            ))}
          </div>
        </div>
      )}
      {!loading && !error && airports.length === 0 && (
        <p>No nearby airports found.</p>
      )}
    </div>
  );
  
};

export default NearbyAirports;
