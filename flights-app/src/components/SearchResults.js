import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useLocation } from 'react-router-dom';

const SearchResults = () => {
  const [flights, setFlights] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [currentPage, setCurrentPage] = useState(1);
  const [flightsPerPage] = useState(5); // Show 5 flights per page
  const [sortOrder, setSortOrder] = useState('lowToHigh'); // Default sort order
  const [durationFilter, setDurationFilter] = useState(null); // Filter by duration

  const location = useLocation();

  const query = new URLSearchParams(location.search);
  const {
    originSkyId = '',
    destinationSkyId = '',
    originEntityId = '',
    destinationEntityId = '',
    date = '',
    returnDate = '',
    cabinClass = 'economy',
    adults = 1,
    childrens = 0,
  } = Object.fromEntries(query.entries());

  useEffect(() => {
    const fetchFlights = async () => {
      if (!originSkyId || !destinationSkyId || !originEntityId || !destinationEntityId || !date) {
        setError("Please provide valid search parameters.");
        setLoading(false);
        return;
      }

      setLoading(true);
      setError(null);

      try {
        const response = await axios.get(`https://sky-scrapper.p.rapidapi.com/api/v2/flights/searchFlights`, {
          params: {
            originSkyId,
            destinationSkyId,
            originEntityId,
            destinationEntityId,
            date,
            returnDate,
            cabinClass,
            adults,
            childrens,
            currency: 'USD',
            market: 'en-US',
            countryCode: 'US',
          },
          headers: {
            'x-rapidapi-host': 'sky-scrapper.p.rapidapi.com',
            'x-rapidapi-key': 'a2b248e679mshf3d81a9f8bc1905p1aef76jsnc9d679aa735c',
          },
        });
        console.log("API Response:", response.data);
        if (response.data?.status) {
          setFlights(response.data.data.itineraries || []);
        } else {
          setFlights([]);
          setError("No flights available for the selected route.");
        }
      } catch (err) {
        setError("An error occurred while fetching flights. Please try again.");
        console.error("API Error:", err.response || err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchFlights();
  }, [originSkyId, destinationSkyId, originEntityId, destinationEntityId, date, returnDate, cabinClass, adults, childrens]);

  // Sorting flights based on price and duration
  const sortedFlights = [...flights].sort((a, b) => {
    const priceA = a.price.total; // Assuming total price is available
    const priceB = b.price.total;

    if (sortOrder === 'lowToHigh') {
      return priceA - priceB; // Sort by price ascending
    } else if (sortOrder === 'highToLow') {
      return priceB - priceA; // Sort by price descending
    }

    return 0; // No sort if order is not recognized
  });

  // Filtering flights based on duration
  const filteredFlights = durationFilter
    ? sortedFlights.filter(itinerary =>
        itinerary.legs.every(leg => leg.durationInMinutes <= durationFilter)
      )
    : sortedFlights;

  // Pagination logic
  const indexOfLastFlight = currentPage * flightsPerPage;
  const indexOfFirstFlight = indexOfLastFlight - flightsPerPage;
  const currentFlights = filteredFlights.slice(indexOfFirstFlight, indexOfLastFlight);

  const handleNextPage = () => {
    if (currentPage < Math.ceil(filteredFlights.length / flightsPerPage)) {
      setCurrentPage(currentPage + 1);
    }
  };

  const handlePreviousPage = () => {
    if (currentPage > 1) {
      setCurrentPage(currentPage - 1);
    }
  };

  return (
    <div className="flight-info-container">
      {loading && <p className="loading-message">Loading flight data...</p>}
      {error && <p className="error-message">{error}</p>}
      {!loading && !error && currentFlights.length > 0 && (
        <div>
          <h1 className="flight-title">Flight Information</h1>
          {currentFlights[0]?.fareAttributes?.destinationImageUrl && (
            <img
              className="destination-image"
              src={currentFlights[0]?.fareAttributes?.destinationImageUrl}
              alt="Destination"
            />
          )}
          <div className="status-info">
            <p>Total Results: <strong>{flights.length}</strong></p>
          </div>

          {/* Sort and Filter Controls */}
          {/* <div className="sort-filter-controls">
            <label>
              Sort by Price:
              <select value={sortOrder} onChange={(e) => setSortOrder(e.target.value)}>
                <option value="lowToHigh">Low to High</option>
                <option value="highToLow">High to Low</option>
              </select>
            </label>
            <label>
              Filter by Duration (minutes):
              <input
                type="number"
                value={durationFilter || ''}
                onChange={(e) => setDurationFilter(e.target.value ? Number(e.target.value) : null)}
                placeholder="Enter max duration"
              />
            </label>
          </div> */}

          <h2 className="itineraries-title">Itineraries</h2>
          {currentFlights.map((itinerary, index) => (
            <div key={index} className="itinerary-card">
              <p className="price">Price: {itinerary.price.formatted}</p>
              <h3 className="legs-title">Legs</h3>
              {itinerary.legs.map((leg, legIndex) => (
                <div key={legIndex} className="leg-info">
                  <p>Departure: <strong>{new Date(leg.departure).toLocaleString()}</strong></p>
                  <p>Arrival: <strong>{new Date(leg.arrival).toLocaleString()}</strong></p>
                  <p>Duration: <strong>{leg.durationInMinutes} minutes</strong></p>
                </div>
              ))}
            </div>
          ))}

          {/* Pagination Controls */}
          <div className="pagination-controls">
            <button onClick={handlePreviousPage} disabled={currentPage === 1}>
              Previous
            </button>
            <span>Page {currentPage} of {Math.ceil(filteredFlights.length / flightsPerPage)}</span>
            <button
              onClick={handleNextPage}
              disabled={currentPage === Math.ceil(filteredFlights.length / flightsPerPage)}
            >
              Next
            </button>
          </div>
        </div>
      )}
      {!loading && !error && currentFlights.length === 0 && (
        <p className="no-flights-message">No flights available for the selected route.</p>
      )}
    </div>
  );
};

export default SearchResults;
