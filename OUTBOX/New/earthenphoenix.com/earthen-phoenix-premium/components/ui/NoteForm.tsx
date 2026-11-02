'use client';
import { useState, type FormEvent } from 'react';
import { AnimatePresence, motion } from 'motion/react';
import { SERVICES } from '@/lib/content';
import { EMAIL, PHONE } from '@/lib/site';
import { Arr } from './Arrow';

/**
 * There is no form inbox yet, so this composes the message in the visitor's own email or text app.
 * Nothing is stored or sent by the website. (Connect Netlify Forms or the GoHighLevel form for a real inbox.)
 */
export default function NoteForm() {
  const [err, setErr] = useState('');
  const [done, setDone] = useState(false);
  const submit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const f = new FormData(e.currentTarget);
    const name = String(f.get('name') || '').trim(), reply = String(f.get('reply') || '').trim(), msg = String(f.get('message') || '').trim();
    if (!name || !reply || !msg) { setErr('Please add your name, a way to reply, and a message.'); return; }
    setErr('');
    const svc = String(f.get('service') || ''), first = f.get('first') ? '\nThis will be my first visit (20% off my first service).' : '';
    const body = `${msg}\n\n${svc ? `Asking about: ${svc}\n` : ''}Reply to: ${reply}${first}\n\n${name}`;
    const url = f.get('how') === 'text'
      ? `sms:+18016094263?&body=${encodeURIComponent(body)}`
      : `mailto:${EMAIL}?subject=${encodeURIComponent(`Note from ${name}${svc ? ` about ${svc}` : ''}`)}&body=${encodeURIComponent(body)}`;
    window.location.href = url;
    setDone(true);
  };
  return (
    <form onSubmit={submit} noValidate className="grid gap-5 rounded-[26px] bg-chalk border border-ink/10 p-6 sm:p-9">
      <p className="kicker text-lichen">Send a note</p>
      <div className="grid gap-5 sm:grid-cols-2">
        <label className="field">Your name<input name="name" autoComplete="name" required /></label>
        <label className="field">Phone or email<input name="reply" autoComplete="email" required /></label>
      </div>
      <label className="field">Asking about
        <select name="service" defaultValue="">
          <option value="">Choose one (optional)</option>
          {SERVICES.map((s) => <option key={s.key}>{s.full}</option>)}
          <option>Products</option><option>Something else</option>
        </select>
      </label>
      <label className="field">Message<textarea name="message" required /></label>
      <label className="flex items-start gap-3 text-[.95rem]"><input type="checkbox" name="first" value="1" className="mt-1 size-4 accent-[var(--color-flame)]" /> This will be my first visit (20% off my first service)</label>
      <fieldset className="flex flex-wrap items-center gap-5 text-[.95rem]">
        <legend className="sr-only">Send it by</legend>
        <span className="text-ink-2">Send it by</span>
        <label className="flex items-center gap-2"><input type="radio" name="how" value="email" defaultChecked className="accent-[var(--color-flame)]" /> Email</label>
        <label className="flex items-center gap-2"><input type="radio" name="how" value="text" className="accent-[var(--color-flame)]" /> Text</label>
      </fieldset>
      <p role="alert" className="text-clay text-sm min-h-5">{err}</p>
      <button type="submit" className="btn btn-flame justify-self-start">Write my message <Arr /></button>
      <p className="text-sm text-ink-2">This opens your own email or text app with your message filled in, ready for you to send. Nothing is stored on this website.</p>
      <AnimatePresence>
        {done && (
          <motion.p initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} className="text-sm text-lichen" role="status">
            Your message should now be open in your email or text app. If nothing opened, write to {EMAIL} or call or text {PHONE}.
          </motion.p>
        )}
      </AnimatePresence>
    </form>
  );
}
