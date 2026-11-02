import { ArrowRight, ArrowUpRight } from 'lucide-react';
export const Arr = ({ out }: { out?: boolean }) => (out ? <ArrowUpRight className="arr" size={18} strokeWidth={1.75} aria-hidden /> : <ArrowRight className="arr" size={18} strokeWidth={1.75} aria-hidden />);
