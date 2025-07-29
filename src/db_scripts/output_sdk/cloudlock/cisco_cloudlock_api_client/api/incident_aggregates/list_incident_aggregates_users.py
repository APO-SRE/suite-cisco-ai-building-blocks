from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_aggregates import IncidentAggregates
from ...models.list_incident_aggregates_users_response_400 import ListIncidentAggregatesUsersResponse400
from ...models.list_incident_aggregates_users_response_401 import ListIncidentAggregatesUsersResponse401
from ...models.list_incident_aggregates_users_response_403 import ListIncidentAggregatesUsersResponse403
from ...models.list_incident_aggregates_users_response_404 import ListIncidentAggregatesUsersResponse404
from ...models.list_incident_aggregates_users_response_500 import ListIncidentAggregatesUsersResponse500
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/incidents/aggregates/users",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        ListIncidentAggregatesUsersResponse400,
        ListIncidentAggregatesUsersResponse401,
        ListIncidentAggregatesUsersResponse403,
        ListIncidentAggregatesUsersResponse404,
        ListIncidentAggregatesUsersResponse500,
        list["IncidentAggregates"],
    ]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = IncidentAggregates.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ListIncidentAggregatesUsersResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ListIncidentAggregatesUsersResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ListIncidentAggregatesUsersResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ListIncidentAggregatesUsersResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ListIncidentAggregatesUsersResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        ListIncidentAggregatesUsersResponse400,
        ListIncidentAggregatesUsersResponse401,
        ListIncidentAggregatesUsersResponse403,
        ListIncidentAggregatesUsersResponse404,
        ListIncidentAggregatesUsersResponse500,
        list["IncidentAggregates"],
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[
        ListIncidentAggregatesUsersResponse400,
        ListIncidentAggregatesUsersResponse401,
        ListIncidentAggregatesUsersResponse403,
        ListIncidentAggregatesUsersResponse404,
        ListIncidentAggregatesUsersResponse500,
        list["IncidentAggregates"],
    ]
]:
    """List Status and Users for Incident Aggregates

     List the status information and users for the incident aggregates.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListIncidentAggregatesUsersResponse400, ListIncidentAggregatesUsersResponse401, ListIncidentAggregatesUsersResponse403, ListIncidentAggregatesUsersResponse404, ListIncidentAggregatesUsersResponse500, list['IncidentAggregates']]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[
        ListIncidentAggregatesUsersResponse400,
        ListIncidentAggregatesUsersResponse401,
        ListIncidentAggregatesUsersResponse403,
        ListIncidentAggregatesUsersResponse404,
        ListIncidentAggregatesUsersResponse500,
        list["IncidentAggregates"],
    ]
]:
    """List Status and Users for Incident Aggregates

     List the status information and users for the incident aggregates.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListIncidentAggregatesUsersResponse400, ListIncidentAggregatesUsersResponse401, ListIncidentAggregatesUsersResponse403, ListIncidentAggregatesUsersResponse404, ListIncidentAggregatesUsersResponse500, list['IncidentAggregates']]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[
        ListIncidentAggregatesUsersResponse400,
        ListIncidentAggregatesUsersResponse401,
        ListIncidentAggregatesUsersResponse403,
        ListIncidentAggregatesUsersResponse404,
        ListIncidentAggregatesUsersResponse500,
        list["IncidentAggregates"],
    ]
]:
    """List Status and Users for Incident Aggregates

     List the status information and users for the incident aggregates.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListIncidentAggregatesUsersResponse400, ListIncidentAggregatesUsersResponse401, ListIncidentAggregatesUsersResponse403, ListIncidentAggregatesUsersResponse404, ListIncidentAggregatesUsersResponse500, list['IncidentAggregates']]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[
        ListIncidentAggregatesUsersResponse400,
        ListIncidentAggregatesUsersResponse401,
        ListIncidentAggregatesUsersResponse403,
        ListIncidentAggregatesUsersResponse404,
        ListIncidentAggregatesUsersResponse500,
        list["IncidentAggregates"],
    ]
]:
    """List Status and Users for Incident Aggregates

     List the status information and users for the incident aggregates.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListIncidentAggregatesUsersResponse400, ListIncidentAggregatesUsersResponse401, ListIncidentAggregatesUsersResponse403, ListIncidentAggregatesUsersResponse404, ListIncidentAggregatesUsersResponse500, list['IncidentAggregates']]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
