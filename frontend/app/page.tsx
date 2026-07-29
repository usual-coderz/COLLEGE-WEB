export default function Home() {
  return (
    <main className="min-h-screen bg-black text-white">
      <nav className="flex items-center justify-between px-8 py-5 border-b border-zinc-800">
        <h1 className="text-2xl font-bold">College Web</h1>

        <div className="flex gap-4">
          <a
            href="/register-college"
            className="px-4 py-2 rounded-lg bg-blue-600"
          >
            Register College
          </a>

          <a
            href="/login"
            className="px-4 py-2 rounded-lg bg-zinc-800"
          >
            Login
          </a>
        </div>
      </nav>

      <section className="max-w-6xl mx-auto px-6 py-24 text-center">
        <h1 className="text-6xl font-bold mb-6">
          Multi College Management Platform
        </h1>

        <p className="text-zinc-400 text-xl mb-10">
          One platform for Notices, Attendance, Notes,
          Events, Placements, Lost & Found and AI Assistant.
        </p>

        <a
          href="/register-college"
          className="px-8 py-4 rounded-xl bg-blue-600 text-lg"
        >
          Get Started
        </a>
      </section>

      <section className="grid md:grid-cols-4 gap-6 max-w-6xl mx-auto px-6 pb-20">
        <div className="bg-zinc-900 p-6 rounded-xl">
          <h2 className="text-xl font-semibold mb-2">
            📢 Notices
          </h2>
          <p className="text-zinc-400">
            Share college notices instantly.
          </p>
        </div>

        <div className="bg-zinc-900 p-6 rounded-xl">
          <h2 className="text-xl font-semibold mb-2">
            📅 Attendance
          </h2>
          <p className="text-zinc-400">
            Manage attendance records.
          </p>
        </div>

        <div className="bg-zinc-900 p-6 rounded-xl">
          <h2 className="text-xl font-semibold mb-2">
            📚 Notes
          </h2>
          <p className="text-zinc-400">
            Upload and share study material.
          </p>
        </div>

        <div className="bg-zinc-900 p-6 rounded-xl">
          <h2 className="text-xl font-semibold mb-2">
            🎯 Placement
          </h2>
          <p className="text-zinc-400">
            Placement preparation hub.
          </p>
        </div>
      </section>
    </main>
  );
}