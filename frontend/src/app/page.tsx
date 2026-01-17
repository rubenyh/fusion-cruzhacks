"use client";

import Image from "next/image";
import { useState } from "react";


export default function Home() {
  const [phone, setPhone] = useState("");
  const [added, setAdded] = useState(false);
  const handleAdd = () => {
    if (!phone.trim()) return;
    setAdded(true);
  };
  return (
    <div className="min-h-screen flex flex-col font-sans">
      <header className="w-full flex justify-center py-6">
        <div className="bg-white rounded-full px-8 py-4 shadow-md">
          <Image
            src="/trashmonlogo.png"
            alt="Trashmon logo"
            width={200}
            height={40}
            priority
          />
        </div>
      </header>

      <main className="flex-1 flex items-center justify-center px-6">
        <div className="w-full max-w-5xl grid grid-cols-1 md:grid-cols-3 gap-6">
            <button className="bg-green-500 hover:bg-blue-700 text-white font-bold py-4 px-4 rounded h-100">View Camera</button>

          <div className="bg-white rounded-2xl shadow-lg border border-gray-200 p-6 md:col-span-2">
            <input
                className="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500"
                type="text"
                placeholder="Enter phone number here: (Format: XXX-XXX-XXXX)"
                value={phone}
                onChange={(e) => {
                  setPhone(e.target.value);
                  setAdded(false);
                }}
              />

              <button
                onClick={handleAdd}
                className="w-full bg-green-600 text-white py-3 rounded-md font-medium hover:bg-green-700 transition disabled:opacity-50 disabled:cursor-not-allowed"
                disabled={!phone.trim()}
              >
                Add
              </button>

              {added && (
                <p className="text-green-600 text-sm text-center">
                  You signed up {phone} for SMS notifications!
                </p>
              )}
              <h2 className="text-gray-600 text-lg mt-4">
                By adding your phone number, you agree to receive SMS notifications
                regarding waste collection schedules and updates. Message and data
                rates may apply. You can opt out at any time by replying STOP to any
                message.
              </h2>
          </div>

        </div>
      </main>
      <footer className="top-20 mb-10 w-full flex justify-center">
          <h2 className="text-lg font-medium">CruzHacks 2024 - Team Fusion</h2>
      </footer>
    </div>
  );
}
