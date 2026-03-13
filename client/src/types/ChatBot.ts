export interface Message {
  text: string;
  dateSent: Date;
  sentBy: "bot" | "customer";
}
