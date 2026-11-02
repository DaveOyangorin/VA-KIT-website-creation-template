/**
 * Every word on the site lives here.
 * Facts come only from earthenphoenix.com and its booking page (/appointment-8682), gathered 30 Oct 2026.
 * Nothing is invented. Inline links in answers use [text](/path).
 */
import type { ImageName } from './images';
import { PHONE, EMAIL } from './site';

export type ServiceKey = 'reiki' | 'swedish' | 'lymph' | 'deep' | 'thai' | 'sarga' | 'zen' | 'yoga' | 'astro' | 'herbs';

export type QA = [question: string, answer: string];

export interface Service {
  key: ServiceKey;
  slug: string;
  name: string;
  full: string;
  price: string;
  length: string;
  line: string;
  /** Where the session sits on the scale of touch, from her own descriptions. */
  touch: string;
  offers: { price: string; label: string }[];
  img: ImageName;
  alt: string;
  pos: string;
  hero: { kicker: string; title: string; answer: string; spec: [string, string][]; pos?: string; img?: ImageName; alt?: string };
  signature: { kicker: string; title: string; body: string[]; hint?: string };
  seo: { title: string; desc: string; ld: string };
  faqs: QA[];
  related: ServiceKey[];
}

const S = (s: Service) => s;

export const SERVICES: Service[] = [
  S({
    key: 'reiki', slug: 'reiki', name: 'Reiki', full: 'Reiki', price: '$130', length: '60 min', touch: 'Hands near',
    line: 'Hands on or near the clothed body', offers: [{ price: '130', label: '60 minutes' }],
    img: 'sound-tuning-forks', alt: 'A client resting on the massage table with tuning forks beside her head', pos: '45% 50%',
    hero: { kicker: 'Energy work · 60 minutes', title: 'Reiki.', answer: 'Hands rest gently on or near your clothed body, to support balance and healing. 60 minutes with a Master Reiki practitioner, $130.', spec: [['Length', '60 min'], ['Price', '$130'], ['Clothing', 'Stay clothed']] },
    signature: { kicker: 'Where her hands rest', title: 'Attention, not pressure.', hint: 'Move across the photograph', body: [
      'A practitioner channels universal energy by gently placing hands on or near the clothed body. Nothing is pushed or kneaded.',
      'Here the light follows your hand without ever touching anything: wherever it rests, the room warms and comes into balance.' ] },
    seo: { title: 'Reiki in Salt Lake City, $130 for 60 Minutes | Earthen Phoenix', desc: 'Reiki in Salt Lake City with Miquelle, a Master Reiki practitioner since 2011. 60 minutes, $130. Hands rest on or near your clothed body.', ld: 'Reiki: hands gently on or near the clothed body to support balance and healing, 60 minutes.' },
    faqs: [
      ['How much does Reiki cost in Salt Lake City?', 'A 60-minute Reiki session is $130.'],
      ['Do I stay clothed for Reiki?', 'Yes. Hands are placed gently on or near your clothed body.'],
      ['What is Reiki?', 'A practitioner channels universal energy by gently placing hands on or near the clothed body to support balance and healing.'],
      ['How long has Miquelle practised Reiki?', 'She started with Reiki in 2011 and is now a Master Reiki practitioner, also trained in sound therapy and breath-work.'],
    ],
    related: ['swedish', 'yoga', 'lymph', 'astro'],
  }),
  S({
    key: 'swedish', slug: 'swedish-massage', name: 'Swedish massage', full: 'Swedish massage', price: '$140 / $170', length: '60 / 90 min', touch: 'Light to medium',
    line: 'Long strokes and essential oils, light to medium pressure', offers: [{ price: '140', label: '60 minutes' }, { price: '170', label: '90 minutes' }],
    img: 'massage-head-neck', alt: 'Miquelle supporting a client’s head and neck during a massage', pos: '50% 30%',
    hero: { kicker: 'Massage · 60 or 90 minutes', title: 'Swedish massage.', answer: 'Long strokes and essential oils at light to medium pressure, for stress relief and relaxation. $140 for 60 minutes or $170 for 90.', spec: [['Length', '60 / 90 min'], ['Price', '$140 / $170'], ['Pressure', 'Light–medium']] },
    signature: { kicker: 'One long stroke at a time', title: 'Warm oil, steady hands.', hint: 'Drag across the photograph', body: [
      'Long strokes and essential oils at light to medium pressure, for stress relief and relaxation.',
      'Draw a stroke across the photograph. Each one leaves a warm, slow trace, the way oil carries the hand the full length of the back.' ] },
    seo: { title: 'Swedish Massage in Salt Lake City, from $140 | Earthen Phoenix', desc: 'Swedish massage in Salt Lake City: long strokes and essential oils at light to medium pressure. $140 for 60 minutes, $170 for 90. Sound therapy and breathwork can be added.', ld: 'Swedish massage: long strokes and essential oils at light to medium pressure; can include sound therapy, meditation and breathwork.' },
    faqs: [
      ['How much is a Swedish massage in Salt Lake City?', '$140 for 60 minutes or $170 for 90 minutes.'],
      ['What pressure is a Swedish massage?', 'Light to medium. For deeper work, see [deep tissue massage](/deep-tissue-massage).'],
      ['Can it include more than massage?', 'Yes: sound therapy, meditation and breathwork, for stress relief and relaxation.'],
    ],
    related: ['deep', 'reiki', 'lymph', 'thai'],
  }),
  S({
    key: 'lymph', slug: 'lymphatic-firming-treatment', name: 'Lymphatic firming', full: 'Lymphatic firming body treatment', price: '$180', length: '90 min', touch: 'Light, flowing',
    line: 'Dry brushing, lymphatic massage, a heated wrap', offers: [{ price: '180', label: '90 minutes' }],
    img: 'reiki-crystals-candles', alt: 'A client resting on the table with candles and crystals around her', pos: '58% 50%',
    hero: { kicker: 'Body treatment · 90 minutes', title: 'Lymphatic firming.', answer: 'A slow, 90-minute full-body treatment in six steps, from dry brushing to a firming cream. $180.', spec: [['Length', '90 min'], ['Price', '$180'], ['Steps', '6']] },
    signature: { kicker: 'The 90 minutes', title: 'Six steps, one slow treatment.', body: [
      'Dry brushing, manual lymphatic massage, a heated body wrap, a hot towel cleanse and a head and neck treatment, finished with Eminence Coconut Firming cream.',
      'Scroll through the treatment. The photograph changes with each step.' ] },
    seo: { title: 'Lymphatic Drainage & Firming Treatment in Salt Lake City, $180 | Earthen Phoenix', desc: 'A 90-minute lymphatic firming body treatment in Salt Lake City for $180: dry brushing, lymphatic massage, heated wrap, hot towel cleanse, head and neck, firming cream.', ld: 'Lymphatic firming body treatment: dry brushing, manual lymphatic massage, heated body wrap, hot towel cleanse, head and neck treatment, Eminence Coconut Firming cream.' },
    faqs: [
      ['How much is the lymphatic firming body treatment?', '$180 for 90 minutes.'],
      ['What is included?', 'Dry brushing, manual lymphatic massage, a heated body wrap, a hot towel cleanse and a head and neck treatment, finished with Eminence Coconut Firming cream.'],
      ['What is it for?', 'The booking page describes it as a treatment for skin firming and for reducing bloating, water retention and inflammation. Choose it for a slow, full-body treatment rather than a pressure-focused massage.'],
    ],
    related: ['swedish', 'reiki', 'zen', 'herbs'],
  }),
  S({
    key: 'deep', slug: 'deep-tissue-massage', name: 'Deep tissue massage', full: 'Deep tissue massage', price: '$150 / $180', length: '60 / 90 min', touch: 'Deep',
    line: 'Deep pressure, breathwork and stretching. Never painful', offers: [{ price: '150', label: '60 minutes' }, { price: '180', label: '90 minutes' }],
    img: 'massage-head-neck', alt: 'Miquelle’s hands working at a client’s neck and shoulders', pos: '30% 62%',
    hero: { kicker: 'Massage · 60 or 90 minutes', title: 'Deep tissue.', answer: 'Deep pressure, breathwork, stretching and movement to restore balance. Therapeutic, and never painful. $150 for 60 minutes or $180 for 90.', spec: [['Length', '60 / 90 min'], ['Price', '$150 / $180'], ['Pressure', 'Deep']], pos: '50% 12%' },
    signature: { kicker: 'Beneath the surface', title: 'Pressure is one part of it.', body: [
      'Deep pressure at the depth you ask for, with breathwork, stretching and movement to restore balance, and stretches to take home.',
      'Scroll to go deeper, one layer at a time.' ] },
    seo: { title: 'Deep Tissue Massage in Salt Lake City, from $150 | Earthen Phoenix', desc: 'Deep tissue massage in Salt Lake City: deep pressure with breathwork, stretching and movement. Therapeutic, never painful. $150 for 60 minutes, $180 for 90.', ld: 'Deep tissue massage: deep pressure, breathwork, stretching and movement to restore balance, with stretching guidance to take home.' },
    faqs: [
      ['How much is a deep tissue massage in Salt Lake City?', '$150 for 60 minutes or $180 for 90 minutes.'],
      ['Is deep tissue massage painful?', 'No. It is therapeutic and never painful. Tell Miquelle how much pressure you want and she adjusts.'],
      ['What else happens besides pressure?', 'Breathwork, stretching and movement to restore balance, plus stretching guidance to take home so the results last.'],
      ['Is there anything deeper?', '[Sarga bodywork](/sarga-bodywork) goes deep into the fascia and suits old injuries. You need to be very comfortable with deep pressure.'],
    ],
    related: ['sarga', 'thai', 'swedish', 'yoga'],
  }),
  S({
    key: 'thai', slug: 'thai-bodywork', name: 'Thai bodywork', full: 'Thai bodywork', price: '$150 / $170', length: '60 / 90 min', touch: 'Rhythm and stretch',
    line: 'Full-body stretching and rhythmic compressions', offers: [{ price: '150', label: '60 minutes' }, { price: '170', label: '90 minutes' }],
    img: 'yoga-assisted-fold', alt: 'Miquelle assisting a stretch on a grassy hillside', pos: '62% 55%',
    hero: { kicker: 'Bodywork · 60 or 90 minutes', title: 'Thai bodywork.', answer: 'Full-body stretching combined with rhythmic compressions. $150 for 60 minutes or $170 for 90.', spec: [['Length', '60 / 90 min'], ['Price', '$150 / $170'], ['Style', 'Rhythm + stretch']], pos: '68% 50%' },
    signature: { kicker: 'Rhythm, then reach', title: 'Pressed on a beat, then drawn long.', hint: 'Tap the photograph to press', body: [
      'Full-body stretching combined with rhythmic compressions. Her booking page describes it as supporting the lymphatic, immune and nervous systems, muscles, tendons and joints.',
      'Watch the photograph take the rhythm, then lengthen. Tap it to add a press of your own.' ] },
    seo: { title: 'Thai Bodywork in Salt Lake City, from $150 | Earthen Phoenix', desc: 'Thai bodywork in Salt Lake City: full-body stretching and rhythmic compressions with Miquelle, certified in Thai bodywork. $150 for 60 minutes, $170 for 90.', ld: 'Thai bodywork: full-body stretching and rhythmic compressions.' },
    faqs: [
      ['How much is Thai massage in Salt Lake City?', 'Thai bodywork is $150 for 60 minutes or $170 for 90 minutes.'],
      ['What happens in Thai bodywork?', 'Full-body stretching combined with rhythmic compressions. Miquelle is certified in Thai bodywork.'],
      ['How is it different from deep tissue?', 'Thai is built on stretching and rhythmic compressions; [deep tissue](/deep-tissue-massage) uses deep pressure with breathwork and stretching.'],
    ],
    related: ['yoga', 'deep', 'sarga', 'swedish'],
  }),
  S({
    key: 'sarga', slug: 'sarga-bodywork', name: 'Sarga bodywork', full: 'Sarga bodywork', price: '$180', length: '90 min', touch: 'Full body weight',
    line: 'Barefoot, with a fabric strap, for old injuries', offers: [{ price: '180', label: '90 minutes' }],
    img: 'sarga-barefoot-strap', alt: 'Miquelle standing barefoot on a client’s back while holding an overhead bar', pos: '50% 28%',
    hero: { kicker: 'Barefoot bodywork · 90 minutes', title: 'Sarga.', answer: 'A barefoot method with a fabric strap, for myofascial and deep tissue work on old injuries. 90 minutes, $180.', spec: [['Length', '90 min'], ['Price', '$180'], ['Pressure', 'Deepest']] },
    signature: { kicker: 'Step by step', title: 'Her whole weight, placed with care.', body: [
      'Miquelle works barefoot, holding a strap overhead so she controls exactly how much weight goes into each step. It reaches into the fascia, for old injuries.',
      'Each step settles the photograph a little further. Take one yourself.' ] },
    seo: { title: 'Sarga Barefoot Bodywork in Salt Lake City, $180 | Earthen Phoenix', desc: 'Sarga bodywork in Salt Lake City: a barefoot method with a fabric strap for deep myofascial work and old injuries. 90 minutes, $180. For people very comfortable with deep pressure.', ld: 'Sarga bodywork: a barefoot method using a fabric strap for myofascial and deep tissue work, intended for old injuries.' },
    faqs: [
      ['How much is Sarga bodywork in Salt Lake City?', '$180 for 90 minutes.'],
      ['Is Sarga uncomfortable?', 'It can be somewhat uncomfortable during the session. You must be very comfortable with deep pressure to receive it.'],
      ['What is Sarga good for?', 'It is a barefoot method using a fabric strap for myofascial and deep tissue work, intended for old injuries.'],
    ],
    related: ['deep', 'thai', 'zen', 'reiki'],
  }),
  S({
    key: 'zen', slug: 'zen-mountain-session', name: 'Zen mountain session', full: 'Zen mountain session', price: '$200', length: '90 min', touch: 'Outdoors',
    line: 'A private massage beside a mountain river', offers: [{ price: '200', label: '90 minutes' }],
    img: 'mountain-meadow', alt: 'A green meadow below steep, snow-streaked mountains', pos: '50% 30%',
    hero: { kicker: 'Outdoors · 90 minutes', title: 'Zen mountain.', answer: 'A private massage beside a peaceful mountain river: therapeutic massage and nature, for relaxation and a reset. 90 minutes, $200.', spec: [['Length', '90 min'], ['Price', '$200'], ['Where', 'By a river']], pos: '62% 40%' },
    signature: { kicker: 'Ninety minutes outside', title: 'Stay. The view opens.', body: [
      'A private massage beside a peaceful mountain river, combining therapeutic massage with nature for relaxation and a reset.',
      'Scroll slowly. The longer you stay, the wider it gets.' ] },
    seo: { title: 'Zen Mountain Massage Session, $200 | Earthen Phoenix', desc: 'The Zen mountain session: a private 90-minute massage beside a peaceful mountain river, $200. Therapeutic massage and nature together for relaxation and a reset.', ld: 'A private 90-minute massage beside a peaceful mountain river, for relaxation and reset.' },
    faqs: [
      ['What is the Zen mountain session?', 'A private massage beside a peaceful mountain river, combining therapeutic massage with nature for relaxation and a reset. 90 minutes.'],
      ['How much is it?', '$200 for 90 minutes.'],
      ['Where is it, and when can I book it?', `Call or text ${PHONE} and ask Miquelle about the location and the season.`],
    ],
    related: ['yoga', 'swedish', 'sarga', 'reiki'],
  }),
  S({
    key: 'yoga', slug: 'private-yoga', name: 'Private yoga', full: 'Private yoga', price: '$140', length: '60 min', touch: 'Your own movement',
    line: 'Vinyasa flow, then slow Yin holds', offers: [{ price: '140', label: '60 minutes, private or split between a group' }],
    img: 'yoga-assisted-fold', alt: 'Miquelle guiding a student into a forward bend on the grass', pos: '40% 50%',
    hero: { kicker: 'Schole yoga · 60 minutes', title: 'Private yoga.', answer: 'Traditional asanas, moving with your own breath: fun Vinyasa flow, then slow Yin holds. $140 for 60 minutes, for you or split with a group.', spec: [['Length', '60 min'], ['Price', '$140'], ['Who', 'You, or a group']], img: 'mountain-meadow', alt: 'Miquelle and a student beginning a yoga practice in a mountain meadow', pos: '28% 50%' },
    signature: { kicker: 'Flow, then hold', title: 'Moving, then still.', hint: 'Switch between flow and hold', body: [
      'Schole yoga: traditional asanas guided to move with your own breath and natural abilities. Fun Vinyasa flow, then slow Yin holds at the end.',
      '“This practice is to guide you into using your own intuition to get into your body and flow verse being told exactly how and when to move.”' ] },
    seo: { title: 'Private Yoga in Salt Lake City, $140 | Earthen Phoenix', desc: 'Private yoga in Salt Lake City with Miquelle: Schole yoga, Vinyasa flow then slow Yin holds, guided by your own breath. $140 for 60 minutes, private or split between a group.', ld: 'Private Schole yoga: Vinyasa flow followed by slow Yin holds, guided by your own breath; private or split between group participants.' },
    faqs: [
      ['How much is private yoga in Salt Lake City?', '$140 for 60 minutes, private or split between group participants.'],
      ['What style of yoga is it?', 'Schole yoga: traditional asanas guided to move with your own breath and natural abilities. Vinyasa flow, then slow Yin holds at the end.'],
      ['Do I need experience?', `The practice guides you to use your own intuition to get into your body and flow, rather than being told exactly how and when to move. Call or text ${PHONE} with any questions.`],
    ],
    related: ['thai', 'reiki', 'zen', 'deep'],
  }),
  S({
    key: 'astro', slug: 'astrology-tarot', name: 'Astrology & tarot', full: 'Astrology & tarot', price: '$2 / min', length: 'By the minute', touch: 'Readings',
    line: 'Birth-chart, tarot and oracle readings', offers: [{ price: '2', label: 'per minute' }],
    img: 'reiki-crystals-candles', alt: 'Lit candles, crystals and a sage bundle around the treatment table', pos: '18% 30%',
    hero: { kicker: 'Readings · $2 a minute', title: 'Astrology and tarot.', answer: 'Birth-chart readings, and tarot and oracle readings about the present moment. $2 per minute.', spec: [['Price', '$2 / min'], ['30 min', '$60'], ['Kinds', 'Chart · Tarot · Oracle']], pos: '30% 40%' },
    signature: { kicker: 'Tarot and oracle', title: 'About the present moment.', hint: 'Turn each card', body: [
      'Tarot empowers you to consider a problem, give a voice to it, work it through and see where the blocks might be. Oracle can provide guidance in a light hearted way.',
      'Astrology offers us a unique understanding of our conscious and subconscious selves, primarily through our birth charts. By exploring our birth chart, we can better understand our personalities and desires, leading to greater self-appreciation, acceptance, and acknowledgment.' ] },
    seo: { title: 'Astrology & Tarot Readings in Salt Lake City, $2/min | Earthen Phoenix', desc: 'Astrology birth-chart readings and tarot or oracle card readings with Miquelle in Salt Lake City, $2 per minute.', ld: 'Astrology readings using birth charts, and tarot or oracle card readings focused on the present moment, at $2 per minute.' },
    faqs: [
      ['How much is an astrology or tarot reading?', '$2 per minute. A 30-minute reading comes to $60.'],
      ['What does an astrology reading cover?', 'It works with your birth chart to explore your personality and desires, toward greater self-appreciation, acceptance and acknowledgment.'],
      ['Tarot or oracle?', 'Both are about the present moment. Tarot helps you consider a problem, give a voice to it, work it through and see where the blocks might be. Oracle can provide guidance in a light-hearted way.'],
    ],
    related: ['herbs', 'reiki', 'yoga', 'zen'],
  }),
  S({
    key: 'herbs', slug: 'herbalism', name: 'Herbalism', full: 'Herbalism consultation', price: 'about $40–$100', length: 'Varies', touch: 'Plants',
    line: 'Custom teas, rollies and tinctures', offers: [],
    img: 'armature-smooth-sailing-face-oil', alt: 'An amber dropper bottle beside fresh rosemary and tumbled crystals', pos: '50% 50%',
    hero: { kicker: '“Plants: those who take care of us.”', title: 'Herbalism.', answer: 'A consultation, then remedies made for you: teas, rollies or tinctures. About $40 to $100.', spec: [['Price', '~$40–$100'], ['Forms', 'Tea · Rollie · Tincture'], ['Herbs arrive', '1–2 weeks']] },
    signature: { kicker: 'Made for you', title: 'Three ways a remedy is made.', hint: 'Choose a remedy', body: [
      'Customized herbal remedies: teas, rollies, and tinctures balance the mind-body and spirit.',
      'A tea steeps slowly and fills the cup; a tincture works a few drops at a time; a rollie goes exactly where you put it.' ] },
    seo: { title: 'Herbalism Consultations & Custom Herbal Remedies, Salt Lake City | Earthen Phoenix', desc: 'Herbalism consultations in Salt Lake City with custom teas, rollies and tinctures made for you. About $40 to $100; herbs arrive from Mountain Rose Herbs in Oregon in 1 to 2 weeks.', ld: 'Herbalism consultation and customized herbal remedies (teas, rollies and tinctures), approximately $40 to $100.' },
    faqs: [
      ['How much is an herbalism consultation?', 'About $40 to $100. Customization, consultation and pricing vary with time and herb prices at the time of purchase.'],
      ['What kind of remedies?', 'Customized herbal remedies: teas, rollies and tinctures.'],
      ['How long do the herbs take?', 'Allow one to two weeks. The herbs come from Mountain Rose Herbs in Oregon.'],
    ],
    related: ['astro', 'reiki', 'lymph', 'yoga'],
  }),
];

export const SERVICE = Object.fromEntries(SERVICES.map((s) => [s.key, s])) as Record<ServiceKey, Service>;
export const bySlug = (slug: string) => SERVICES.find((s) => s.slug === slug);

/** The home page groups the sessions by how her hands meet the body, from her own descriptions. */
export const REGISTER: { title: string; note: string; keys: ServiceKey[] }[] = [
  { title: 'Hands near', note: 'No pressure at all.', keys: ['reiki'] },
  { title: 'Hands that glide', note: 'Light to medium, long and slow.', keys: ['swedish', 'lymph'] },
  { title: 'Hands that press', note: 'Deep, rhythmic, never painful.', keys: ['deep', 'thai'] },
  { title: 'Full weight', note: 'For people very comfortable with deep pressure.', keys: ['sarga'] },
  { title: 'Beyond the table', note: 'Place, movement, readings and plants.', keys: ['zen', 'yoga', 'astro', 'herbs'] },
];

export const VOICES = [
  { quote: 'This is not your typical spa massage where you leave feeling underwhelmed and overcharged.', name: 'Sylvie' },
  { quote: 'Miquelle is like the Thanos of massage, she’s has collected all of the massage techniques in existence.', name: 'V' },
  { quote: 'I was pregnant and it was the first time I was pain free the entire pregnancy.', name: 'Megan' },
];

export const PRODUCTS = [
  { name: 'Armature Aurora Signature Body Oil', price: '$44', img: 'armature-aurora-body-oil' as ImageName, alt: 'Two amber bottles of Armature Aurora body oil on a white shell dish', store: 'aurora' as const },
  { name: 'Armature Smooth Sailing Face Oil', price: '$55', img: 'armature-smooth-sailing-face-oil' as ImageName, alt: 'Armature Smooth Sailing face oil beside fresh rosemary and tumbled crystals', store: 'sailing' as const },
  { name: 'M’s Secret Body Butter', price: '$44', img: 'ms-secret-body-butter' as ImageName, alt: 'A jar of M’s Secret body butter in front of a glowing salt lamp', store: 'butter' as const },
];

export const CERTS: { name: string; path?: string }[] = [
  { name: 'Sarga', path: '/sarga-bodywork' }, { name: 'Lymphatic', path: '/lymphatic-firming-treatment' }, { name: 'Thai Bodywork', path: '/thai-bodywork' },
  { name: 'Cupping' }, { name: 'Cranial-Sacral Therapy' }, { name: 'Sound Therapy' }, { name: 'Reflexology' },
  { name: 'Yoga', path: '/private-yoga' }, { name: 'Reiki', path: '/reiki' }, { name: 'Breath-Work' },
];

export const ABOUT_WORDS = [
  'I have spent the last thirteen years learning the integrative aspects that include the mind, body, and spirit. I started with Reiki in 2011 and am now a Master Reiki practitioner. I graduated from the Utah College of Massage Therapy in 2012.',
  'I have worked with many different people, backgrounds, and bodies. Everyone is extremely unique. I base my work off individual needs; and can accommodate anything from light and relaxing to deep fascial work.',
  'I believe in all modalities that work for you. I have learned through my own experiences that by working with the practitioner and modalities that call to you, you innately empower your own ability to heal.',
  'I teach and practice yoga as well as meditation. I am grateful to facilitate space for anyone who is looking to heal. Thank you for your time and I look forward to working together.',
];

export const SESSIONS_FAQ: QA[] = [
  ['How much is a massage at Earthen Phoenix?', 'Swedish massage starts at $140 for 60 minutes. Deep tissue is $150 / $180 and Thai bodywork $150 / $170 (60 / 90 minutes). The lymphatic firming treatment and Sarga are $180 for 90 minutes, and the Zen mountain session is $200 for 90 minutes.'],
  ['Is there a first-time discount?', 'Yes. Mention you are a first-time client when you book for 20% off your first service.'],
  ['Which session is right for me?', `For no pressure at all, Reiki. For relaxation, Swedish. For deep work, deep tissue or Sarga. Still unsure? Call or text ${PHONE} and Miquelle will help you choose.`],
];

export const ALL_FAQ: { title: string; items: QA[] }[] = [
  { title: 'Booking and visiting', items: [
    ['Where is Earthen Phoenix?', 'In Salt Lake City, Utah. The Zen mountain session takes place outdoors beside a mountain river; ask Miquelle about its location and season.'],
    ['How do I book?', `Use the [online booking page](BOOK), call or text ${PHONE}, or email ${EMAIL}.`],
    ['Is there a first-time discount?', 'Yes. Mention you are a first-time client for 20% off your first service.'],
    ['Which session should I choose?', 'See how each one works on [Sessions & prices](/sessions). Still unsure? Call or text and Miquelle will help you choose.'],
  ] },
  { title: 'Massage and bodywork', items: [
    ['How much does a massage cost?', 'Swedish $140 / $170, deep tissue $150 / $180, Thai bodywork $150 / $170 (60 / 90 minutes). Lymphatic firming and Sarga are $180 for 90 minutes; the Zen mountain session is $200 for 90 minutes.'],
    ['Is deep tissue painful?', 'No. It is therapeutic and never painful.'],
    ['Is Sarga uncomfortable?', 'It can be somewhat uncomfortable. You must be very comfortable with deep pressure to receive it.'],
    ['What is in the lymphatic firming treatment?', 'Dry brushing, manual lymphatic massage, a heated body wrap, a hot towel cleanse and a head and neck treatment, finished with Eminence Coconut Firming cream.'],
  ] },
  { title: 'Reiki and yoga', items: [
    ['Do I stay clothed for Reiki?', 'Yes. Hands are placed gently on or near the clothed body. $130 for 60 minutes.'],
    ['Can I share a yoga session?', 'Yes. $140 for 60 minutes, private or split between group participants.'],
  ] },
  { title: 'Readings and remedies', items: [
    ['How are readings priced?', 'Astrology, tarot and oracle readings are $2 per minute.'],
    ['How long do herbal remedies take?', 'Allow one to two weeks for herbs to arrive from Mountain Rose Herbs in Oregon. Consultations are about $40 to $100.'],
  ] },
  { title: 'About Miquelle', items: [
    ['What is Miquelle’s training?', 'Reiki since 2011, now a Master Reiki practitioner; Utah College of Massage Therapy, 2012; certified in Sarga, lymphatic, Thai bodywork, cupping, cranial-sacral therapy, sound therapy, reflexology, yoga, Reiki and breath-work.'],
  ] },
];
