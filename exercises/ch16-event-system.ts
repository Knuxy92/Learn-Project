type UserEvent =
  | { type: "login"; userName: string }
  | { type: "logout"; userId: number }
  | { type: "error"; message: string };

const printEvent = (event: UserEvent): void => {
  const event_type = event.type;
  const message =
    event_type === "login"
      ? event.userName
      : event_type === "logout"
        ? event.userId
        : event_type === "error"
          ? event.message
          : "";
  console.log(
    `${event_type.charAt(0).toUpperCase() + event_type.slice(1)}: ${message}`,
  );
};

const isString = (value: unknown): value is string => {
  return typeof value === "string";
};

const safeUpperCase = (value: unknown): string => {
  if (isString(value)) return value.toUpperCase();
  return "NOT A STRING";
};

type EventHandler = (event: UserEvent) => void;

const handleEvent: EventHandler = (event): void => printEvent(event);

handleEvent({ type: "login", userName: "Knuxy92" });
handleEvent({ type: "logout", userId: 17 });
handleEvent({ type: "error", message: "Something went wrong" });

console.log(safeUpperCase("hello"));
console.log(safeUpperCase(123));
