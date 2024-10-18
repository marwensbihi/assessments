import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Home = () => {
  const locations = [
    { skyId: 'NYCA', entityId: '27537542', title: 'New York', subtitle: 'United States' },
    { skyId: 'EWR', entityId: '95565059', title: 'New York Newark', subtitle: 'United States' },
    { skyId: 'JFK', entityId: '95565058', title: 'New York John F. Kennedy', subtitle: 'United States' },
    { skyId: 'LGA', entityId: '95565057', title: 'New York LaGuardia', subtitle: 'United States' },
    { skyId: 'SWF', entityId: '95566280', title: 'Stewart International', subtitle: 'United States' },
    { skyId: 'NCL', entityId: '95674044', title: 'Newcastle', subtitle: 'United Kingdom' },
    { skyId: 'NQY', entityId: '95673963', title: 'Newquay', subtitle: 'United Kingdom' },
    { skyId: 'NZ', entityId: '29475342', title: 'New Zealand', subtitle: '' },
    // Add more locations as needed
  ];

  const [originSkyId, setOriginSkyId] = useState('');
  const [destinationSkyId, setDestinationSkyId] = useState('');
  const [originEntityId, setOriginEntityId] = useState('');
  const [destinationEntityId, setDestinationEntityId] = useState('');
  const [date, setDate] = useState('');
  const [returnDate, setReturnDate] = useState('');
  const [cabinClass, setCabinClass] = useState('economy');
  const [adults, setAdults] = useState(1);
  const [children, setChildren] = useState(0);
  const [sortBy, setSortBy] = useState('best');
  const [currency, setCurrency] = useState('USD');
  const [market, setMarket] = useState('en-US');
  const [countryCode, setCountryCode] = useState('US');
  const navigate = useNavigate();

  const handleSearch = (e) => {
    e.preventDefault();

    if (!originSkyId || !destinationSkyId || !originEntityId || !destinationEntityId || !date) {
      alert('Please fill in all the required fields.');
      return;
    }

    const queryParams = new URLSearchParams({
      originSkyId,
      destinationSkyId,
      originEntityId,
      destinationEntityId,
      date,
      returnDate,
      cabinClass,
      adults,
      children,
      sortBy,
      currency,
      market,
      countryCode,
    }).toString();

    navigate(`/search?${queryParams}`);
  };

  const handleOriginChange = (e) => {
    const selectedSkyId = e.target.value;
    setOriginSkyId(selectedSkyId);

    const selectedLocation = locations.find(location => location.skyId === selectedSkyId);
    if (selectedLocation) {
      setOriginEntityId(selectedLocation.entityId);
    }
  };

  const handleDestinationChange = (e) => {
    const selectedSkyId = e.target.value;
    setDestinationSkyId(selectedSkyId);

    const selectedLocation = locations.find(location => location.skyId === selectedSkyId);
    if (selectedLocation) {
      setDestinationEntityId(selectedLocation.entityId);
    }
  };

  return (
    <div className="home-container">
      {/* Button for Nearby Airports */}
      <button
        className="nearby-airports-button"
        onClick={() => navigate('/nearby-airports')}
        style={{
          position: 'absolute',
          top: '10px',
          right: '10px',
          padding: '10px',
          backgroundColor: '#007bff',
          color: '#fff',
          border: 'none',
          borderRadius: '5px',
          cursor: 'pointer',
        }}
      >
        Nearby Airports
      </button>
      <h2>Search Flights</h2>
      <form onSubmit={handleSearch} className="flight-search-form">
        <div className="form-group">
          <label htmlFor="originSkyId">Origin</label>
          <select id="originSkyId" value={originSkyId} onChange={handleOriginChange} required>
            <option value="">Select Origin</option>
            {locations.map((location) => (
              <option key={location.skyId} value={location.skyId}>
                {location.title} ({location.skyId}) - {location.subtitle}
              </option>
            ))}
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="destinationSkyId">Destination</label>
          <select id="destinationSkyId" value={destinationSkyId} onChange={handleDestinationChange} required>
            <option value="">Select Destination</option>
            {locations.map((location) => (
              <option key={location.skyId} value={location.skyId}>
                {location.title} ({location.skyId}) - {location.subtitle}
              </option>
            ))}
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="date">Departure Date</label>
          <input
            type="date"
            id="date"
            value={date}
            onChange={(e) => setDate(e.target.value)}
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="returnDate">Return Date (Optional)</label>
          <input
            type="date"
            id="returnDate"
            value={returnDate}
            onChange={(e) => setReturnDate(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label htmlFor="cabinClass">Cabin Class</label>
          <select
            id="cabinClass"
            value={cabinClass}
            onChange={(e) => setCabinClass(e.target.value)}
          >
            <option value="economy">Economy</option>
            <option value="premium_economy">Premium Economy</option>
            <option value="business">Business</option>
            <option value="first">First</option>
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="adults">Adults (12+ years)</label>
          <input
            type="number"
            id="adults"
            value={adults}
            onChange={(e) => setAdults(Math.max(1, e.target.value))}
            min="1"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="children">Children (2-12 years)</label>
          <input
            type="number"
            id="children"
            value={children}
            onChange={(e) => setChildren(Math.max(0, e.target.value))}
            min="0"
          />
        </div>
        <div className="form-group">
          <label htmlFor="sortBy">Sort By</label>
          <select
            id="sortBy"
            value={sortBy}
            onChange={(e) => setSortBy(e.target.value)}
          >
            <option value="best">Best</option>
            <option value="price_high">Cheapest</option>
            <option value="fastest">Fastest</option>
            <option value="outbound_take_off_time">Outbound Take Off Time</option>
            <option value="outbound_landing_time">Outbound Landing Time</option>
            <option value="return_take_off_time">Return Take Off Time</option>
            <option value="return_landing_time">Return Landing Time</option>
          </select>
        </div>
        <div className="form-group">
          <button type="submit" className="search-button">Search Flights</button>
        </div>
      </form>
    </div>
  );
};

export default Home;
